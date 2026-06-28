class Usuario():

    def __init__(self, nombre, apellido, dni, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo

    def set_nombre(self, nuevo):
        self.nombre = nuevo

    def set_apellido(self, nuevo):
        self.apellido = nuevo

    def set_dni(self, nuevo):
        self.dni = nuevo

    def set_correo(self, nuevo):
        self.correo = nuevo

    def __str__(self):
        return (
            f"Nombre: {self.nombre} {self.apellido} | "
            f"DNI: {self.dni} | "
            f"Correo: {self.correo}"
        )
