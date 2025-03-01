import os

import reflex as rx

database_url = os.getenv("DATABASE_URL", "sqlite:///reflex.db")

config = rx.Config(
    app_name="App_Hernan_reflex",
    db_url="sqlite:///reflex.db",
    env= rx.Env.DEV
)