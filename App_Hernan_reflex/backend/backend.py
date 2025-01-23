import reflex as rx

from sqlmodel import String, asc, cast, desc, func, or_, select

class Cliente(rx.Model, table=True):
    nombre:str
    identificacion: int
    email:str
    telefono:int  
    direccion:str


class ClienteState(rx.State):
    users: list[Cliente] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_user: Cliente = Cliente()    
    
    def load_clientes(self) -> list[Cliente]:
        with rx.session() as session:
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
    
    
    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_clientes()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_clientes()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_clientes()

    def get_user(self, user: Cliente):
        self.current_user = user
            
    def add_cliente_to_db(self, form_data: dict):
        with rx.session() as session:
            if session.exec(
                select(Cliente).where(Cliente.identificacion == form_data.get("identificacion"))
            ).first():
                return rx.window_alert("El usuario con esa identificación ya existe")
            self.current_user = Cliente(
                # date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                **form_data
            )
            session.add(self.current_user)
            session.commit()
            session.refresh(self.current_user)
        self.load_clientes()
        return rx.toast.info(
            f"El cliente {self.current_user.nombre} ha sido agregado exitosamente.", position="bottom-right"
        )

    def update_customer_to_db(self, form_data: dict):
        with rx.session() as session:
            customer = session.exec(
                select(Cliente).where(Cliente.identificacion == self.current_user.identificacion)
            ).first()
            form_data.pop("identificacion", None)
            customer.set(**form_data)
            session.add(customer)
            session.commit()
        self.load_clientes()
        return rx.toast.info(
            f"El cliente {self.current_user.nombre} fue modificado.",
            position="bottom-right",
        )

    def delete_customer(self, identificacion: int):
        """Delete a customer from the database."""
        with rx.session() as session:
            customer = session.exec(select(Cliente).where(Cliente.identificacion == identificacion)).first()
            session.delete(customer)
            session.commit()
        self.load_clientes()
        return rx.toast.info(
            f"El cliente {customer.nombre} fue Eliminado.", position="bottom-right"
        )
