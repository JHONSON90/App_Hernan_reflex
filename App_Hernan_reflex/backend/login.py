import reflex as rx

class AuthState(rx.State):
    username: str = ""
    password: str = ""
    error_message: str = ""
    is_authenticated: bool = False

    # Credenciales predefinidas (puedes cambiarlas)
    VALID_USERNAME = "williamportilla40@gmail.com"
    VALID_PASSWORD = "marisol123"

    def set_username(self, value: str):
        self.username = value

    def set_password(self, value: str):
        self.password = value

    @rx.event
    async def handle_login(self, form_data: dict):
        print("Handling login with data:", form_data)
        username = form_data.get("username")
        password = form_data.get("password")

        # Verificar las credenciales
        if username == self.VALID_USERNAME and password == self.VALID_PASSWORD:
            print("Login successful")
            self.is_authenticated = True
            self.error_message = ""
            self.username = username
            # Redirigir a la página principal
            yield rx.redirect("/transacciones")
        else:
            self.error_message = "Usuario o contraseña incorrectos"
            self.is_authenticated = False

    def logout(self):
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/")
    
    @rx.event
    def check_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/")