from datetime import date, datetime


# 1. CLASE PARA GUARDAR LAS OPERACIONES 

# Representa una operación realizada dentro del sistema.
# Los registros se almacenarán en una lista, no en diccionarios.
class RegistroOperacion:

    def __init__(self, operacion, fecha_hora, detalle):
        self.operacion = operacion
        self.fecha_hora = fecha_hora
        self.detalle = detalle

    def __str__(self):
        return (
            f"{self.fecha_hora.strftime('%d/%m/%Y %H:%M:%S')} | "
            f"{self.operacion} | "
            f"{self.detalle}"
        )


# 2. DECORADOR PROPIO


# Registra automáticamente una operación después de ejecutar
# el método decorado.
def auditar(nombre_operacion):

    # Recibe el método original.
    def decorador(funcion_original):

        # Esta función reemplaza temporalmente al método original.
        def envoltura(self, *argumentos):

            # Ejecuta el método original.
            resultado = funcion_original(self, *argumentos)

            # Crea el registro de la operación.
            nuevo_registro = RegistroOperacion(
                nombre_operacion,
                datetime.now(),
                str(resultado)
            )

            # Guarda el registro dentro de la biblioteca.
            self.registros.append(nuevo_registro)

            # Devuelve el resultado original.
            return resultado

        return envoltura

    return decorador

# ==========================================================
# METACLASE CREADA MEDIANTE TYPE
# ==========================================================

def crear_clase_estado(
    metaclase,
    nombre,
    bases,
    espacio_nombres
):
    nueva_clase = type.__new__(
        metaclase,
        nombre,
        bases,
        espacio_nombres
    )

    if nombre != "EstadoPrestamo":

        metodos_obligatorios = (
            "esta_activo",
            "devolver",
            "descripcion"
        )

        faltantes = []

        for metodo in metodos_obligatorios:
            if metodo not in espacio_nombres:
                faltantes.append(metodo)

        if len(faltantes) > 0:
            raise TypeError(
                f"La clase {nombre} debe implementar: "
                f"{', '.join(faltantes)}"
            )

    return nueva_clase


# Crea una metaclase que hereda de type.
MetaEstadoPrestamo = type(
    "MetaEstadoPrestamo",
    (type,),
    {
        "__module__": __name__,
        "__new__": crear_clase_estado
    }
)


# ==========================================================
# CLASE BASE ESTADO PRESTAMO
# ==========================================================

def estado_esta_activo(self):
    raise NotImplementedError(
        "La clase hija debe implementar esta_activo()."
    )


def estado_devolver(self, prestamo):
    raise NotImplementedError(
        "La clase hija debe implementar devolver()."
    )


def estado_descripcion(self):
    raise NotImplementedError(
        "La clase hija debe implementar descripcion()."
    )


EstadoPrestamo = MetaEstadoPrestamo(
    "EstadoPrestamo",
    (object,),
    {
        "__module__": __name__,
        "esta_activo": estado_esta_activo,
        "devolver": estado_devolver,
        "descripcion": estado_descripcion
    }
)


# ==========================================================
# ESTADO ACTIVO
# ==========================================================

def activo_esta_activo(self):
    return True


def activo_devolver(self, prestamo):
    prestamo.fecha_devolucion = date.today()
    prestamo._cambiar_estado(EstadoDevuelto())

    return True


def activo_descripcion(self):
    return "Activo"


EstadoActivo = MetaEstadoPrestamo(
    "EstadoActivo",
    (EstadoPrestamo,),
    {
        "__module__": __name__,
        "esta_activo": activo_esta_activo,
        "devolver": activo_devolver,
        "descripcion": activo_descripcion
    }
)


# ==========================================================
# ESTADO DEVUELTO
# ==========================================================

def devuelto_esta_activo(self):
    return False


def devuelto_devolver(self, prestamo):
    return False


def devuelto_descripcion(self):
    return "Devuelto"


EstadoDevuelto = MetaEstadoPrestamo(
    "EstadoDevuelto",
    (EstadoPrestamo,),
    {
        "__module__": __name__,
        "esta_activo": devuelto_esta_activo,
        "devolver": devuelto_devolver,
        "descripcion": devuelto_descripcion
    }
)

#CLASE LIBRO

class Libro:

    # Crea un libro con sus datos mínimos.
    def __init__(self, titulo, autor, isbn, publicacion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.publicacion = publicacion
        self.paginas = paginas

    # Modifica el título.
    def set_titulo(self, nuevo):
        self.titulo = nuevo

    # Modifica el autor.
    def set_autor(self, nuevo):
        self.autor = nuevo

    # Modifica el ISBN.
    def set_isbn(self, nuevo):
        self.isbn = nuevo

    # Modifica el año de publicación.
    def set_publicacion(self, nuevo):
        self.publicacion = nuevo

    # Modifica la cantidad de páginas.
    def set_paginas(self, nuevo):
        self.paginas = nuevo

    # Devuelve los datos del libro en forma de texto.
    def __str__(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn} | "
            f"Año de publicación: {self.publicacion} | "
            f"Páginas: {self.paginas}"
        )


# ==========================================================
# 6. CLASE USUARIO
# ==========================================================

class Usuario:

    # Crea un usuario con sus datos mínimos.
    def __init__(self, nombre, apellido, dni, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo

    # Modifica el nombre.
    def set_nombre(self, nuevo):
        self.nombre = nuevo

    # Modifica el apellido.
    def set_apellido(self, nuevo):
        self.apellido = nuevo

    # Modifica el DNI.
    def set_dni(self, nuevo):
        self.dni = nuevo

    # Modifica el correo electrónico.
    def set_correo(self, nuevo):
        self.correo = nuevo

    # Devuelve los datos del usuario en forma de texto.
    def __str__(self):
        return (
            f"Nombre: {self.nombre} {self.apellido} | "
            f"DNI: {self.dni} | "
            f"Correo: {self.correo}"
        )


# ==========================================================
# 7. CLASE PRÉSTAMO
# ==========================================================

class Prestamo:

    # Crea un préstamo relacionando un libro con un usuario.
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

        # COMPOSICIÓN:
        # El préstamo crea y administra internamente su estado.
        self.__estado = EstadoActivo()

    # Delega la consulta al objeto que representa el estado.
    def esta_activo(self):
        return self.__estado.esta_activo()

    # Delega la devolución al estado actual.
    def registrar_devolucion(self):
        return self.__estado.devolver(self)

    # Devuelve el nombre del estado actual.
    def obtener_estado(self):
        return self.__estado.descripcion()

    # Cambia internamente el estado del préstamo.
    def _cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    # Devuelve los datos del préstamo en forma de texto.
    def __str__(self):

        if self.fecha_devolucion is None:
            devolucion = "Pendiente"
        else:
            devolucion = self.fecha_devolucion

        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} "
            f"{self.usuario.apellido} | "
            f"Fecha de préstamo: {self.fecha_prestamo} | "
            f"Fecha de devolución: {devolucion} | "
            f"Estado: {self.obtener_estado()}"
        )


# ==========================================================
# 8. CLASE BIBLIOTECA
# ==========================================================

class Biblioteca:

    # Crea las listas utilizadas por la biblioteca.
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.registros = []

    # ------------------------------------------------------
    # BÚSQUEDAS
    # ------------------------------------------------------

    # Busca un libro por ISBN.
    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro

        return None

    # Busca un usuario por DNI.
    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario

        return None

    # ------------------------------------------------------
    # GESTIÓN DE LIBROS
    # ------------------------------------------------------

    # Da de alta un libro.
    # El decorador registra automáticamente la operación.
    @auditar("Alta de libro")
    def agregar_l(self, libro):

        if self.buscar_libro(libro.isbn) is not None:
            return "Ya existe un libro con ese ISBN."

        # AGREGACIÓN:
        # La biblioteca recibe un libro creado externamente.
        self.libros.append(libro)

        return f"Libro agregado: {libro.titulo}"

    # Modifica los datos de un libro existente.
    @auditar("Modificación de libro")
    def modificar_libro(
        self,
        isbn_actual,
        nuevo_titulo,
        nuevo_autor,
        nuevo_isbn,
        nueva_publicacion,
        nuevas_paginas
    ):
        libro = self.buscar_libro(isbn_actual)

        if libro is None:
            return "No existe un libro con ese ISBN."

        # Busca si el nuevo ISBN pertenece a otro libro.
        libro_con_nuevo_isbn = self.buscar_libro(nuevo_isbn)

        if (
            libro_con_nuevo_isbn is not None
            and libro_con_nuevo_isbn is not libro
        ):
            return "Ya existe otro libro con el nuevo ISBN."

        libro.set_titulo(nuevo_titulo)
        libro.set_autor(nuevo_autor)
        libro.set_isbn(nuevo_isbn)
        libro.set_publicacion(nueva_publicacion)
        libro.set_paginas(nuevas_paginas)

        return f"Libro modificado: {libro.titulo}"

    # Da de baja un libro por ISBN.
    @auditar("Baja de libro")
    def retirar_l(self, isbn):
        libro = self.buscar_libro(isbn)

        if libro is None:
            return "No existe un libro con ese ISBN."

        # No permite eliminar un libro prestado.
        if self.verificar_prestamo_activo(isbn):
            return (
                "No se puede retirar el libro porque "
                "posee un préstamo activo."
            )

        self.libros.remove(libro)

        return f"Libro retirado: {libro.titulo}"

    # Devuelve la lista de libros.
    def listar_libros(self):
        return self.libros

    # ------------------------------------------------------
    # GESTIÓN DE USUARIOS
    # ------------------------------------------------------

    # Da de alta un usuario.
    @auditar("Alta de usuario")
    def agregar_u(self, usuario):

        if self.buscar_usuario(usuario.dni) is not None:
            return "Ya existe un usuario con ese DNI."

        # AGREGACIÓN:
        # La biblioteca recibe un usuario creado externamente.
        self.usuarios.append(usuario)

        return (
            f"Usuario agregado: "
            f"{usuario.nombre} {usuario.apellido}"
        )

    # Modifica los datos de un usuario.
    @auditar("Modificación de usuario")
    def modificar_usuario(
        self,
        dni_actual,
        nuevo_nombre,
        nuevo_apellido,
        nuevo_dni,
        nuevo_correo
    ):
        usuario = self.buscar_usuario(dni_actual)

        if usuario is None:
            return "No existe un usuario con ese DNI."

        usuario_con_nuevo_dni = self.buscar_usuario(nuevo_dni)

        if (
            usuario_con_nuevo_dni is not None
            and usuario_con_nuevo_dni is not usuario
        ):
            return "Ya existe otro usuario con el nuevo DNI."

        usuario.set_nombre(nuevo_nombre)
        usuario.set_apellido(nuevo_apellido)
        usuario.set_dni(nuevo_dni)
        usuario.set_correo(nuevo_correo)

        return (
            f"Usuario modificado: "
            f"{usuario.nombre} {usuario.apellido}"
        )

    # Da de baja un usuario por DNI.
    @auditar("Baja de usuario")
    def retirar_u(self, dni):
        usuario = self.buscar_usuario(dni)

        if usuario is None:
            return "No existe un usuario con ese DNI."

        # Comprueba si el usuario tiene préstamos activos.
        for prestamo in self.prestamos:
            if (
                prestamo.usuario is usuario
                and prestamo.esta_activo()
            ):
                return (
                    "No se puede retirar el usuario porque "
                    "posee un préstamo activo."
                )

        self.usuarios.remove(usuario)

        return (
            f"Usuario retirado: "
            f"{usuario.nombre} {usuario.apellido}"
        )

    # Devuelve la lista de usuarios.
    def listar_usuarios(self):
        return self.usuarios

    # ------------------------------------------------------
    # GESTIÓN DE PRÉSTAMOS
    # ------------------------------------------------------

    # Verifica si un libro posee un préstamo activo.
    def verificar_prestamo_activo(self, isbn):
        for prestamo in self.prestamos:
            if (
                prestamo.libro.isbn == isbn
                and prestamo.esta_activo()
            ):
                return True

        return False

    # Registra un préstamo.
    @auditar("Registro de préstamo")
    def registrar_prestamo(self, isbn, dni):
        libro = self.buscar_libro(isbn)

        if libro is None:
            return "No existe un libro con ese ISBN."

        usuario = self.buscar_usuario(dni)

        if usuario is None:
            return "No existe un usuario con ese DNI."

        # Impide prestar un libro que ya está prestado.
        if self.verificar_prestamo_activo(isbn):
            return "El libro ya posee un préstamo activo."

        nuevo_prestamo = Prestamo(libro, usuario)
        self.prestamos.append(nuevo_prestamo)

        return nuevo_prestamo

    # Registra la devolución de un libro.
    @auditar("Registro de devolución")
    def registrar_devolucion(self, isbn):

        for prestamo in self.prestamos:
            if (
                prestamo.libro.isbn == isbn
                and prestamo.esta_activo()
            ):
                prestamo.registrar_devolucion()
                return prestamo

        return "No existe un préstamo activo para ese libro."

    # Devuelve solamente los préstamos activos.
    def obtener_prestamos_activos(self):
        prestamos_activos = []

        for prestamo in self.prestamos:
            if prestamo.esta_activo():
                prestamos_activos.append(prestamo)

        return prestamos_activos

    # Devuelve todos los registros creados por el decorador.
    def listar_registros(self):
        return self.registros

    def __str__(self):
        return (
            f"Libros: {len(self.libros)} | "
            f"Usuarios: {len(self.usuarios)} | "
            f"Préstamos: {len(self.prestamos)} | "
            f"Registros: {len(self.registros)}"
        )