import reflex as rx
from sqlmodel import SQLModel
from App_Hernan_reflex.backend.backend import Cliente  # Ajusta esta importación a tu estructura de proyecto

def init_db():
    """Inicializa la base de datos."""
    with rx.session() as session:
        SQLModel.metadata.create_all(session.bind)
        print("Base de datos inicializada")

if __name__ == "__main__":
    init_db()