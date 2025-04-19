import reflex as rx
from ..backend.login import AuthState

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color="black",underline="never", align="center"), 
        href=url, 
        
    )


def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/William-Portilla.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "WP", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Clientes", "/usuarios"),
                    navbar_link("Transacciones", "/transacciones"),
                    rx.button(
                        rx.text(
                            "Cerrar Sesion",
                            size="4",
                            weight="medium",
                        ),
                        variant="solid",
                        color_scheme="blue",
                        size="3",
                        on_click=AuthState.logout,
                    ),
                    justify="end",
                    spacing="5",
                    align="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/William-Portilla.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "WP", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Clientes", on_click=lambda: rx.redirect("/usuarios")),
                        rx.menu.item("Transacciones", on_click=lambda: rx.redirect("/transacciones")),
                        rx.menu.item("Cerrar sesion", on_click=AuthState.logout),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("orange",9),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )