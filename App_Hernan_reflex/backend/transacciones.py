import reflex as rx

from datetime import datetime
import asyncio

from sqlmodel import String, asc, cast, desc, func, or_,select, SQLModel, Field

#from .backend import Cliente

class Transaccion(rx.Model, table=True):
    id_transaccion: int = Field(default=None, primary_key=True)
    fecha: str
    cliente_identificacion: int
    tipo_transaccion: str
    usuario_final: str
    total_recibido: int
    valor_transaccion: int
    

class TransaccionState(rx.State):
    transacciones: list[Transaccion] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_transaccion: Transaccion = Transaccion()    
    
    def on_mount(self):
        return self.load_transacciones()
    
    @rx.event
    async def on_load_transacciones(self) -> list[Transaccion]:
        with rx.session() as session:
            all_transacciones = session.exec(select(Transaccion)).all()
            print("Transacciones cargadas", len(all_transacciones))
            self.transacciones = session.exec(select(Transaccion)).all()
            query = select(Transaccion)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Transaccion, field).ilike(search_value)
                            for field in Transaccion.get_fields()
                        ],
                    )
                )
            if self.sort_value:
                sort_column = getattr(Transaccion, self.sort_value)
                if self.sort_value == "id_transaccion":
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                else:
                    order = (
                        desc(func.lower(sort_column))
                        if self.sort_reverse
                        else asc(func.lower(sort_column))
                    )
                query = query.order_by(order)
                
            self.transacciones = session.exec(query).all()
            
    @rx.event
    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.on_load_transacciones()
        
    @rx.event
    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.on_load_transacciones()
        
    @rx.event
    def filter_values(self, search_value):
        self.search_value = search_value
        self.on_load_transacciones()
        
    # @rx.event
    # def get_transa_unit(self, transaccion: Transaccion):
    #     self.current_transaccion = transaccion
    
    @rx.event
    def get_transa_unit(self, transaccion: Transaccion):
        with rx.session() as session:
            # Obtener la transacción desde la base de datos usando el ID
            db_transaccion = session.exec(
                select(Transaccion).where(Transaccion.id_transaccion == transaccion.id_transaccion)
            ).first()
            if db_transaccion:
                self.current_transaccion = db_transaccion
            else:
                rx.toast.error("No se encontró la transacción", position="bottom-right", duration=3000)
            
    # @rx.event
    # def get_transaccion(self, id_transaccion: int):
    #     with rx.session() as session:
    #         self.current_transaccion
    
    @rx.event
    def get_transaccion(self, id_transaccion: int):
        with rx.session() as session:
            transaccion = session.exec(select(Transaccion).where(Transaccion.id_transaccion == id_transaccion)).first()
            if transaccion:
                self.current_transaccion = transaccion
            
    @rx.event
    async def add_transaccion(self, form_data: dict):
        print("Intentando guardar transaccion:", form_data)
        try:
            print("Transaccion recibida", form_data)
            form_data["fecha"] = datetime.now().strftime("%d-%m-%Y")
            #cambiar los tipos de datos que se reciben a int o float
            form_data["cliente_identificacion"] = int(form_data["cliente_identificacion"])
            form_data["total_recibido"] = int(form_data["total_recibido"])
            form_data["valor_transaccion"] = int(form_data["valor_transaccion"])
            print("Transaccion recibida")
            with rx.session() as session:
                nueva_transaccion = Transaccion(**form_data)
                print("Transaccion recibida", nueva_transaccion)
                session.add(nueva_transaccion)
                session.commit()
                session.refresh(nueva_transaccion)
                
                self.transacciones.append(nueva_transaccion)
                #self.current_transaccion = nueva_transaccion
                print("Transaccion agregada")
                
                await self.load_transacciones()
                
                return rx.toast.success("Transaccion agregada exitosamente", position="bottom-right", duration=5000)
            
        except Exception as e:
            print("el error es:",e)
            return rx.toast.error("Error al agregar transaccion", position="bottom-right", duration=5000)
        
    @rx.event
    async def update_transaccion(self, form_data: dict):
        try:
            with rx.session() as session:
                transaccion = session.exec(select(Transaccion).where(Transaccion.id_transaccion == self.current_transaccion.id_transaccion)).first()
                if transaccion:
                    form_data.pop("id_transaccion", None)
                    form_data["fecha"]= datetime.now().strftime("%d-%m-%Y")
                    for key, value in form_data.items():
                        setattr(transaccion, key, value)
                    session.add(transaccion)
                    session.commit()
                    session.refresh(transaccion)
                    self.current_transaccion = transaccion
                    yield rx.set_value("dialog", False)
                        
                    await self.load_transacciones()
                        
                    rx.toast.success(f"La transaccion {self.current_transaccion.id_transaccion} fue modificada", position="bottom-right", duration=3000)
                
                else:
                    rx.toast.error("No se encontró la transaccion", position="bottom-right", duration=3000)
        except Exception as e:
            rx.toast.error("Error al actualizar transaccion", position="bottom-right", duration=3000)
            
    @rx.event
    async def delete_transaccion(self, id_transaccion: int):
        try:
            with rx.session() as session:
                transaccion = session.exec(select(Transaccion).where(Transaccion.id_transaccion == id_transaccion)).first()
                if transaccion:
                    id_transaccion = transaccion.id_transaccion
                    session.delete(transaccion)
                    session.commit()
                    
                    self.transacciones = [t for t in self.transacciones if t.id_transaccion != id_transaccion]
                    await self.load_transacciones()
                    return rx.toast.success(f"La transaccion {id_transaccion} fue eliminada", position="bottom-right", duration=3000)
            #return rx.toast.error("No se encontró la transaccion", position="bottom-right", duration=3000)
        except Exception as e:
            return rx.toast.error("Error al eliminar transaccion", position="bottom-right", duration=3000)