from requerimientos_tecnicos import auditar, Prestamo


class Biblioteca():

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.registros = []

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    # No permite agregar un libro si ya existe otro con el mismo ISBN.
    @auditar("Alta de libro")
    def agregar_l(self, libro):
        if self.buscar_libro(libro.isbn) is not None:
            return "Ya existe un libro con ese ISBN."

        self.libros.append(libro)
        return f"Libro agregado: {libro.titulo}"

    @auditar("Modificación de libro")
    def modificar_libro(self, isbn_actual, nuevo_titulo, nuevo_autor, nuevo_isbn, nueva_publicacion, nuevas_paginas):
        libro = self.buscar_libro(isbn_actual)

        if libro is None:
            return "No existe un libro con ese ISBN."

        otro = self.buscar_libro(nuevo_isbn)
        if otro is not None and otro is not libro:
            return "Ya existe otro libro con el nuevo ISBN."

        libro.set_titulo(nuevo_titulo)
        libro.set_autor(nuevo_autor)
        libro.set_isbn(nuevo_isbn)
        libro.set_publicacion(nueva_publicacion)
        libro.set_paginas(nuevas_paginas)

        return f"Libro modificado: {libro.titulo}"

    @auditar("Baja de libro")
    def retirar_l(self, isbn):
        libro = self.buscar_libro(isbn)

        if libro is None:
            return "No existe un libro con ese ISBN."

        if self.verificar_prestamo_activo(isbn):
            return "No se puede retirar el libro porque posee un préstamo activo."

        self.libros.remove(libro)
        return f"Libro retirado: {libro.titulo}"

    def listar_libros(self):
        return self.libros

    @auditar("Alta de usuario")
    def agregar_u(self, usuario):
        if self.buscar_usuario(usuario.dni) is not None:
            return "Ya existe un usuario con ese DNI."

        self.usuarios.append(usuario)
        return f"Usuario agregado: {usuario.nombre} {usuario.apellido}"

    @auditar("Modificación de usuario")
    def modificar_usuario(self, dni_actual, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo):
        usuario = self.buscar_usuario(dni_actual)

        if usuario is None:
            return "No existe un usuario con ese DNI."

        otro = self.buscar_usuario(nuevo_dni)
        if otro is not None and otro is not usuario:
            return "Ya existe otro usuario con el nuevo DNI."

        usuario.set_nombre(nuevo_nombre)
        usuario.set_apellido(nuevo_apellido)
        usuario.set_dni(nuevo_dni)
        usuario.set_correo(nuevo_correo)

        return f"Usuario modificado: {usuario.nombre} {usuario.apellido}"

    @auditar("Baja de usuario")
    def retirar_u(self, dni):
        usuario = self.buscar_usuario(dni)

        if usuario is None:
            return "No existe un usuario con ese DNI."

        for prestamo in self.prestamos:
            if prestamo.usuario is usuario and prestamo.esta_activo():
                return "No se puede retirar el usuario porque posee un préstamo activo."

        self.usuarios.remove(usuario)
        return f"Usuario retirado: {usuario.nombre} {usuario.apellido}"

    def listar_usuarios(self):
        return self.usuarios

    # Devuelve True si el libro tiene un préstamo sin devolver.
    def verificar_prestamo_activo(self, isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.esta_activo():
                return True
        return False

    # Verifica que el libro y el usuario existan y que el libro esté disponible antes de registrar el préstamo.
    @auditar("Registro de préstamo")
    def registrar_prestamo(self, isbn, dni):
        libro = self.buscar_libro(isbn)
        if libro is None:
            return "No existe un libro con ese ISBN."

        usuario = self.buscar_usuario(dni)
        if usuario is None:
            return "No existe un usuario con ese DNI."

        if self.verificar_prestamo_activo(isbn):
            return "El libro ya posee un préstamo activo."

        nuevo_prestamo = Prestamo(libro, usuario)
        self.prestamos.append(nuevo_prestamo)
        return nuevo_prestamo

    @auditar("Registro de devolución")
    def registrar_devolucion(self, isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.esta_activo():
                prestamo.registrar_devolucion()
                return prestamo

        return "No existe un préstamo activo para ese libro."

    def obtener_prestamos_activos(self):
        prestamos_activos = []

        for prestamo in self.prestamos:
            if prestamo.esta_activo():
                prestamos_activos.append(prestamo)

        return prestamos_activos

    def listar_registros(self):
        return self.registros

    def __str__(self):
        return (
            f"Libros: {len(self.libros)} | "
            f"Usuarios: {len(self.usuarios)} | "
            f"Préstamos: {len(self.prestamos)} | "
            f"Registros: {len(self.registros)}"
        )
