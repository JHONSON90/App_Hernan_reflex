import reflex as rx

from ..backend.backend import Cliente, ClienteState
from ..components.form_field import form_field
#from ..components.status_badges import status_badge


def show_customer(user: Cliente):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.nombre),
        rx.table.cell(user.identificacion),
        rx.table.cell(user.email),
        rx.table.cell(user.telefono),
        rx.table.cell(user.direccion),
        
        rx.table.cell(
            rx.hstack(
                #update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: ClienteState.delete_customer(user.identificacion),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"background": rx.color("gray", 3)}},
        align="center",
    )


def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Adicionar Cliente", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Adicionar Cliente",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Llena el formulario para crear un nuevo cliente",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form(
                    rx.flex(
                        # Name
                        form_field(
                            "Nombres y Apellidos",
                            "Nombres del cliente",
                            "text",
                            "nombre",  # Cambiado de "name" a "nombre"
                            "user",
                        ),
                        #identificacion
                        form_field(
                            "Identificacion",
                            "Identificacion",
                            "number",
                            "identificacion",
                            "fingerprint",
                        ),
                        # Email
                        form_field(
                            "Email", 
                            "user@reflex.dev", 
                            "email", 
                            "email", 
                            "mail"
                        ),
                        # Phone
                        form_field(
                            "Telefono", 
                            "Telefono del cliente", 
                            "tel", 
                            "telefono",  # Cambiado de "phone" a "telefono"
                            "phone"
                        ),
                        # Address
                        form_field(
                            "Direccion", 
                            "Direccion del cliente", 
                            "text", 
                            "direccion",  # Cambiado de "address" a "direccion"
                            "home"
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        #rx.dialog.close(
                            rx.button(
                            "Guardar",
                            type="submit"
                            ),
                        #),
                        
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=ClienteState.add_cliente_to_db,
                    reset_on_submit=True,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


# def update_customer_dialog(user):
#     return rx.dialog.root(
#         rx.dialog.trigger(
#             rx.button(
#                 rx.icon("square-pen", size=22),
#                 rx.text("Editar", size="3"),
#                 color_scheme="blue",
#                 size="2",
#                 variant="solid",
#                 on_click=lambda: ClienteState.get_user(user),
#             ),
#         ),
#         rx.dialog.content(
#             rx.hstack(
#                 rx.badge(
#                     rx.icon(tag="square-pen", size=34),
#                     color_scheme="grass",
#                     radius="full",
#                     padding="0.65rem",
#                 ),
#                 rx.vstack(
#                     rx.dialog.title(
#                         "Editar Cliente",
#                         weight="bold",
#                         margin="0",
#                     ),
#                     rx.dialog.description(
#                         "Editar la informacion del cliente",
#                     ),
#                     spacing="1",
#                     height="100%",
#                     align_items="start",
#                 ),
#                 height="100%",
#                 spacing="4",
#                 margin_bottom="1.5em",
#                 align_items="center",
#                 width="100%",
#             ),
#             rx.flex(
#                 rx.form(
#                     rx.flex(
#                         # Name
#                         form_field(
#                             "Nombre",
#                             "Nombre del cliente",
#                             "text",
#                             "nombre",
#                             "user",
#                             user.nombre,
#                         ),
#                         # Identificacion
#                         form_field(
#                             "Identificacion",
#                             "Identificacion",
#                             "number",
#                             "identificacion",
#                             "fingerprint",
#                             user.identificacion.to(str),
#                         ),
                        
#                         # Email
#                         form_field(
#                             "Email",
#                             "user@reflex.dev",
#                             "email",
#                             "email",
#                             "mail",
#                             user.email,
#                         ),
#                         # Phone
#                         form_field(
#                             "Telefono",
#                             "Telefono del cliente",
#                             "tel",
#                             "telefono",
#                             "phone",
#                             user.telefono.to(str),
#                         ),
#                         # Address
#                         form_field(
#                             "Direccion",
#                             "Direccion del cliente",
#                             "text",
#                             "direccion",
#                             "home",
#                             user.direccion,
#                         ),
#                         direction="column",
#                         spacing="3",
#                     ),
#                     rx.flex(
#                         rx.dialog.close(
#                             rx.button(
#                                 "Cancel",
#                                 variant="soft",
#                                 color_scheme="gray",
#                             ),
#                         ),
#                         rx.dialog.close(
#                             rx.button(
#                             "Actualizar Cliente",
#                             type="submit"
#                             ),
#                         ),
                        
#                             #as_child=True,
#                         padding_top="2em",
#                         spacing="3",
#                         mt="4",
#                         justify="end",
#                         ),
#                         on_submit=ClienteState.update_customer_to_db,
#                         reset_on_submit=True,
#                     ),
#                 width="100%",
#                 direction="column",
#                 spacing="4",
#                 ),
#             max_width="450px",
#             padding="1.5em",
#             border=f"2px solid {rx.color('accent', 7)}",
#             border_radius="25px",
#             ),
            
#         ),



def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            rx.heading("Clientes", size="9", weight="bold"),
            add_customer_button(),
            rx.spacer(),
            rx.cond(
                ClienteState.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=ClienteState.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=ClienteState.toggle_sort,
                ),
            ),
            rx.select(
                ["nombre", "identificacion", "email", "telefono", "direccion"], #"date", "status"
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: ClienteState.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aqui...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: ClienteState.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Nombre", "user"),
                    _header_cell("Identificacion", "fingerprint"),
                    _header_cell("Email", "mail"),
                    _header_cell("Telefono", "phone"),
                    _header_cell("Direccion", "home"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(ClienteState.users, show_customer)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=ClienteState.load_clientes,
        ),
    )