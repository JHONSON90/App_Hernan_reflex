import reflex as rx
from ..backend.login import AuthState

def login_default_icons() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/William-Portilla.png",
                        width="4.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Iniciar sesion",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        name="username",
                        size="3",
                        width="100%",
                        on_change=AuthState.set_username,
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Olvidaste tu contraseña?",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        name="password",
                        size="3",
                        width="100%",
                        on_change=AuthState.set_password,
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Iniciar Sesion", 
                        size="3", 
                        width="100%",
                        type="submit",
                        ),
                rx.cond(
                    AuthState.error_message,
                    rx.text(AuthState.error_message, color="red"),
                ),
                spacing="6",
                width="100%",
                ),
            on_submit=AuthState.handle_login,
            width="100%",
            
            ),
        max_width="28em",
        size="4",
        width="100%",
    )
