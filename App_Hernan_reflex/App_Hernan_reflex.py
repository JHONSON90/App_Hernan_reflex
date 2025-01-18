"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from App_Hernan_reflex.views.login import login_default_icons
from App_Hernan_reflex.views.signup import signup_default_icons
from App_Hernan_reflex.views.user_table import main_table
from App_Hernan_reflex.views.dash_transaccion import transacciones

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def inicio() -> rx.Component:
    return rx.container(
        login_default_icons()
    )
    
def registro() -> rx.Component:
    return rx.container(
        signup_default_icons()
        )
    
def tabla() -> rx.Component:
    return rx.vstack(
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )

def transacciones_dash() -> rx.Component:
    return rx.vstack(
        rx.box(
            transacciones(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )
    

app = rx.App()
app.add_page(index)
app.add_page(inicio)
app.add_page(registro)
app.add_page(tabla)
app.add_page(transacciones_dash)
