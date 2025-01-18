import reflex as rx

#from ..backend.backend import Customer, State
from ..components.form_field import form_field
#from ..components.status_badges import status_badge


def show_customer():
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.identificacion),
        rx.table.cell(user.name),
        rx.table.cell(user.tipo),
        rx.table.cell(user.usuario_final),
        rx.table.cell(f"${user.payments_total:,}"),
        rx.table.cell(f"${user.payments_cobro:,}"),
        
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    #on_click=lambda: State.delete_customer(user.id),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
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
                            "identificacion",
                            "fingerprint",
                        ),
                        # Name
                        form_field(
                            "Nombres y Apellidos",
                            "Nombres del cliente",
                            "text",
                            "name",
                            "user",
                        ),
                        
                        # Email
                        form_field(
                            "Tipo", "Tipo de transacción", "text", "tipo", "credit-card"
                        ),
                        # Phone
                        form_field("Usuario Final", "A quien le consignas?", "text", "usuario_final", "user-round-check"),
                        # Pago total
                        form_field(
                            "Total Recibido ($)",
                            "Total Transacción",
                            "number",
                            "payments",
                            "dollar-sign",
                        ),
                        # cunto cobro
                        form_field(
                            "Pago Recibido ($)",
                            "TCuanto cobras al cliente",
                            "number",
                            "payments",
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
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Guardar"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    #on_submit=State.add_customer_to_db,
                    #reset_on_submit=False,
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


def update_customer_dialog(user):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                #on_click=lambda: State.get_user(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Editar Transacción",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Editar la Transacción",
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
                            "identificacion",
                            "fingerprint",
                        ),
                        # Name
                        form_field(
                            "Nombres y Apellidos",
                            "Nombres del cliente",
                            "text",
                            "name",
                            "user",
                        ),
                        
                        # Email
                        form_field(
                            "Tipo", "Tipo de transacción", "text", "tipo", "credit-card"
                        ),
                        # Phone
                        form_field("Usuario Final", "A quien le consignas?", "text", "usuario_final", "user-round-check"),
                        # Pago total
                        form_field(
                            "Total Recibido ($)",
                            "Total Transacción",
                            "number",
                            "payments",
                            "dollar-sign",
                        ),
                        # cunto cobro
                        form_field(
                            "Pago Recibido ($)",
                            "TCuanto cobras al cliente",
                            "number",
                            "payments",
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
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Cambiar Transacción"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    #on_submit=State.update_customer_to_db,
                    #reset_on_submit=False,
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


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def transacciones():
    return rx.fragment(
        rx.flex(
            add_transaccion_button(),
            rx.spacer(),
            rx.cond(
                #State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    #on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    #on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                ["identificacion", "name",  "tipo", "usuario_final", "payments_total", "payments_cobro"], #"date", "status"
                placeholder="Sort By: Name",
                size="3",
                #on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aqui...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                #on_change=lambda value: State.filter_values(value),
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
                    _header_cell("Nombre", "user"),
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
            # rx.table.body(rx.foreach(State.users, show_customer)),
            # variant="surface",
            # size="3",
            # width="100%",
            #on_mount=State.load_entries,
        ),
    )