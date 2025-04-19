import reflex as rx

from datetime import datetime
from sqlmodel import select
from ..backend.transacciones import Transaccion, TransaccionState
from ..components.form_field import form_field
#from ..components.status_badges import status_badge
#from ..backend.backend import Cliente


def show_customer(user:Transaccion):
    return rx.table.row(
        rx.table.cell(user.cliente_identificacion),
        #rx.table.cell(rx.computed_fn(TransaccionState.get_customer_name)(user.cliente_identificacion)),
        rx.table.cell(user.tipo_transaccion),
        rx.table.cell(user.usuario_final),
        rx.table.cell(f"${user.total_recibido:,}"),
        rx.table.cell(f"${user.valor_transaccion:,}"),
        
        rx.table.cell(
            rx.hstack(
                #update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: TransaccionState.delete_transaccion(user.id_transaccion),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"background": rx.color("gray", 3)}},
        align="center",
    )

def add_transaccion_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Adicionar Transaccion", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="circle-dollar-sign", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Adicionar Transacción",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Colocar los registros de tus clientes",
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
                rx.form.root(
                    rx.flex(
                        #identificacion
                        form_field(
                            "Identificacion",
                            "Identificacion",
                            "number",
                            "cliente_identificacion",
                            "fingerprint",
                        ),
                        # Name
                        # form_field(
                        #     "Nombres y Apellidos",
                        #     "Nombres del cliente",
                        #     "text",
                        #     "name",
                        #     "user",
                        # ),
                        
                        # Email
                        form_field(
                            "Tipo", "Tipo de transacción", "text", "tipo_transaccion", "credit-card"
                        ),
                        # Phone
                        form_field("Usuario Final", "A quien le consignas?", "text", "usuario_final", "user-round-check"),
                        # Pago total
                        form_field(
                            "Total Recibido ($)",
                            "Total Transacción",
                            "number",
                            "total_recibido",
                            "dollar-sign",
                        ),
                        # cuanto cobro
                        form_field(
                            "Pago Recibido ($)",
                            "Cuanto cobras al cliente",
                            "number",
                            "valor_transaccion",
                            "dollar-sign",
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
                                type="submit",
                            ),
                        #),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=TransaccionState.add_transaccion,
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
#                 rx.text("Edit", size="3"),
#                 color_scheme="blue",
#                 size="2",
#                 variant="solid",
#                 on_click=lambda: TransaccionState.get_transa_unit(user),
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
#                         "Editar Transacción",
#                         weight="bold",
#                         margin="0",
#                     ),
#                     rx.dialog.description(
#                         "Editar la Transacción",
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
#                 rx.form.root(
#                     rx.flex(
#                         #identificacion
#                         form_field(
#                             "Identificacion",
#                             "Identificacion",
#                             "number",
#                             "cliente_identificacion",
#                             "fingerprint",
#                             TransaccionState.current_transaccion.cliente_identificacion
#                             #user.cliente_identificacion,
#                         ),
#                         # Name
#                         # form_field(
#                         #     "Nombres y Apellidos",
#                         #     "Nombres del cliente",
#                         #     "text",
#                         #     "name",
#                         #     "user",
#                         #     rx.computed_fn(TransaccionState.get_customer_name)(user.cliente_identificacion),
#                         # ),
                        
                        
#                         # Email
#                         form_field(
#                             "Tipo", "Tipo de transacción", "text", "tipo_transaccion", "credit-card",
#                             TransaccionState.current_transaccion.tipo_transaccion
#                             #user.tipo_transaccion
#                         ),
#                         # Phone
#                         form_field("Usuario Final", "A quien le consignas?", "text", "usuario_final", "user-round-check",
#                                    TransaccionState.current_transaccion.usuario_final
#                                    #user.usuario_final
#                                    ),
#                         # Pago total
#                         form_field(
#                             "Total Recibido ($)",
#                             "Total Transacción",
#                             "number",
#                             "total_recibido",
#                             "dollar-sign",
#                             TransaccionState.current_transaccion.total_recibido
#                             #user.total_recibido
#                         ),
#                         # cunto cobro
#                         form_field(
#                             "Pago Recibido ($)",
#                             "Cuanto cobras al cliente",
#                             "number",
#                             "valor_transaccion",
#                             "dollar-sign",
#                             TransaccionState.current_transaccion.valor_transaccion
#                             #user.valor_transaccion
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
                        
#                         rx.button(
#                             "Cambiar Transacción",
#                             type="submit",
#                             ),
                            
#                         padding_top="2em",
#                         spacing="3",
#                         mt="4",
#                         justify="end",
#                     ),
#                     on_submit=TransaccionState.update_transaccion,
#                     reset_on_submit=True,
#                 ),
#                 width="100%",
#                 direction="column",
#                 spacing="4",
#             ),
#             max_width="450px",
#             padding="1.5em",
#             border=f"2px solid {rx.color('accent', 7)}",
#             border_radius="25px",
#         ),
#     )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def transacciones_page():
    return rx.fragment(
        rx.flex(
            rx.heading("Transacciones", size="9", weight="bold"),
            add_transaccion_button(),
            rx.spacer(),
            rx.cond(
                TransaccionState.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=TransaccionState.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=TransaccionState.toggle_sort,
                ),
            ),
            rx.select(
                ["cliente_identificacion",  "tipo_transaccion", "usuario_final", "total_recibido", "valor_transaccion"], #"date", "status"
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: TransaccionState.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aqui...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: TransaccionState.filter_values(value),
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
                    _header_cell("Identificacion", "fingerprint"),
                    #_header_cell("Nombre", "user"),
                    _header_cell("Tipo", "credit-card"),
                    _header_cell("Usuario Final", "user-round-check"),
                    _header_cell("Pago Total", "dollar-sign"),
                    _header_cell("Total Cobrado", "dollar-sign"),
                    #_header_cell("Pagos", "dollar-sign"),
                    #_header_cell("Date", "calendar"),
                    #_header_cell("Status", "truck"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(TransaccionState.transacciones, show_customer)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=TransaccionState.on_load_transacciones,
        ),
    )