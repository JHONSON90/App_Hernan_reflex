import reflex as rx
import asyncio

from sqlmodel import String, asc, cast, desc, func, or_, select, SQLModel, Field

class Cliente(rx.Model, table=True):
    nombre:str
    identificacion: int = Field(unique=True, primary_key=True)
    email:str
    telefono:int  
    direccion:str


class ClienteState(rx.State):
    users: list[Cliente] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_user: Cliente = Cliente()    
    
    def on_mount(self):
        return self.load_clientes()
    
    @rx.event
    async def load_clientes(self) -> list[Cliente]:
        with rx.session() as session:
            self.users = session.exec(select(Cliente)).all()
            print("Numero de clientes cargados", len(self.users))
            query = select(Cliente)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Cliente, field).ilike(search_value)
                            for field in Cliente.get_fields()
                        ],
                    )
                )

            if self.sort_value:
                sort_column = getattr(Cliente, self.sort_value)
                if self.sort_value == "identificacion":
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                else:
                    order = (
                        desc(func.lower(sort_column))
                        if self.sort_reverse
                        else asc(func.lower(sort_column))
                    )
                query = query.order_by(order)

            self.users = session.exec(query).all()
            print("clientes cargados satisfactoriamente")
    
    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_clientes()
        
    @rx.event
    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_clientes()

    @rx.event
    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_clientes()

    @rx.event
    def get_user(self, user: Cliente):
        self.current_user = user
            
    @rx.event
    async def add_cliente_to_db(self, form_data: dict):
        """Agregar un nuevo cliente a la base de datos."""
        try:
            with rx.session() as session:
                # Verificar si ya existe el cliente
                existing_client = session.exec(
                    select(Cliente).where(
                        Cliente.identificacion == form_data.get("identificacion")
                    )
                ).first()
                
                if existing_client:
                    return rx.window_alert("El usuario con esa identificación ya existe")
                
                # Crear nuevo cliente
                nuevo_cliente = Cliente(**form_data)
                session.add(nuevo_cliente)
                session.commit()
                session.refresh(nuevo_cliente)
                
                # Actualizar el cliente actual
                self.current_user = nuevo_cliente
                
                # Recargar la lista de clientes
                await self.load_clientes()
                
                return rx.toast.success(
                    f"Cliente {nuevo_cliente.nombre} agregado exitosamente",
                    position="bottom-right",
                    duration=5000
                )
                
        except Exception as e:
            print(f"Error al agregar cliente: {str(e)}")
            return rx.toast.error(
                "Error al agregar el cliente",
                position="bottom-right",
                duration=3000
            )
        
    @rx.event
    async def update_customer_to_db(self, form_data: dict):
        try:
            with rx.session() as session:
                customer = session.exec(
                    select(Cliente).where(Cliente.identificacion == self.current_user.identificacion)
                ).first()
                if customer:
                    form_data.pop("identificacion", None)
                    for key, value in form_data.items():
                        setattr(customer, key, value)
                    
                    session.add(customer)
                    session.commit()
                    session.refresh(customer)
                    
                    self.current_user = customer
                    yield rx.set_value("dialog", False)
                    
                    await self.load_clientes()
                
                    rx.toast.success(
                        f"El cliente {self.current_user.nombre} fue modificado.",
                        position="bottom-right",
                        duration=3000
                    )
                else:
                    rx.toast.error(
                    "No se encontró el cliente para actualizar",
                    position="bottom-right",
                    duration=3000
                )
        except Exception as e:
            print(f"Error al actualizar cliente: {str(e)}")
            rx.toast.error( 
            "Error al actualizar el cliente",
            position="bottom-right",
            duration=3000
        )
                        
            
        
    @rx.event
    async def delete_customer(self, identificacion: int):
        try:
            with rx.session() as session:
                customer = session.exec(select(Cliente).where(Cliente.identificacion == identificacion)).first()
                
                if customer:
                    nombre = customer.nombre
                    session.delete(customer)
                    session.commit()
                    
                    self.users = [u for u in self.users if u.identificacion != identificacion]
                    await self.load_clientes()
                return rx.toast.info(
                    f"El cliente {customer.nombre} fue Eliminado.", position="bottom-right",
                    duration=3000,
                )
            return rx.toast.error(
                    "Cliente no encontrado",
                    position="bottom-right"
                )
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return rx.toast.error(
                "Error al eliminar cliente",
                position="bottom-right"
            )