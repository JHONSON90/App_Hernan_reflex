"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from App_Hernan_reflex.views.login import login_default_icons
from App_Hernan_reflex.views.signup import signup_default_icons
from App_Hernan_reflex.views.user_table import main_table
from App_Hernan_reflex.views.dash_transaccion import transacciones_page
from App_Hernan_reflex.components.navbar import navbar_dropdown
from App_Hernan_reflex.backend.login import AuthState

def inicio() -> rx.Component:
    return rx.container(
        login_default_icons()
    )
    
def registro() -> rx.Component:
    return rx.container(
        signup_default_icons()
        )
    
def tabla() -> rx.Component:
    return rx.fragment(
        rx.cond(
            AuthState.is_authenticated,
            rx.vstack(
                navbar_dropdown(),
                rx.box(
                    rx.spacer(height="2em"),
                    main_table(),
                    width="100%",
                ),
                width="100%",
                spacing="6",
                padding_x=["1.5em", "1.5em", "3em"],
            ),
            rx.text("No estás autenticado. Redirigiendo..."),
        ),
        on_mount=AuthState.check_auth,
    )

def transacciones_dashboard() -> rx.Component:
    return rx.fragment(
        rx.cond(
            AuthState.is_authenticated,
            rx.vstack(
                navbar_dropdown(),
                rx.box(
                    rx.spacer(height="2em"),
                    transacciones_page(),
                    width="100%",
                ),
                width="100%",
                spacing="6",
                padding_x=["1.5em", "1.5em", "3em"],
            ),
            rx.text("No estás autenticado. Redirigiendo..."),
        ),
        on_mount=AuthState.check_auth,  # Verifica autenticación al cargar la página
    )
    
       
app = rx.App()
app.add_page(transacciones_dashboard, route="/transacciones")
app.add_page(inicio, route="/")
app.add_page(registro, route="/registro")
app.add_page(tabla, route="/usuarios")
