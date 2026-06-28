from datetime import date, datetime


class RegistroOperacion():

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


# Decorador que registra automáticamente cada operación en la lista de registros de la biblioteca.
def auditar(nombre_operacion):

    def decorador(funcion_original):

        def wrapper(self, *argumentos):
            resultado = funcion_original(self, *argumentos)

            nuevo_registro = RegistroOperacion(
                nombre_operacion,
                datetime.now(),
                str(resultado)
            )

            self.registros.append(nuevo_registro)
            return resultado

        return wrapper

    return decorador


# Valida que toda subclase de EstadoPrestamo implemente los métodos obligatorios.
def _crear_clase_estado(metaclase, nombre, bases, espacio_nombres):
    nueva_clase = type.__new__(metaclase, nombre, bases, espacio_nombres)

    if nombre != "EstadoPrestamo":
        metodos_obligatorios = ("esta_activo", "devolver", "descripcion")
        faltantes = []

        for metodo in metodos_obligatorios:
            if metodo not in espacio_nombres:
                faltantes.append(metodo)

        if faltantes:
            raise TypeError(
                f"La clase {nombre} debe implementar: {', '.join(faltantes)}"
            )

    return nueva_clase


# Metaclase creada con type que controla la construcción de las clases de estado.
MetaEstadoPrestamo = type(
    "MetaEstadoPrestamo",
    (type,),
    {
        "__module__": __name__,
        "__new__": _crear_clase_estado
    }
)


def _base_esta_activo(self):
    raise NotImplementedError("esta_activo()")

def _base_devolver(self, prestamo):
    raise NotImplementedError("devolver()")

def _base_descripcion(self):
    raise NotImplementedError("descripcion()")


EstadoPrestamo = MetaEstadoPrestamo(
    "EstadoPrestamo",
    (object,),
    {
        "__module__": __name__,
        "esta_activo": _base_esta_activo,
        "devolver": _base_devolver,
        "descripcion": _base_descripcion
    }
)


def _activo_esta_activo(self):
    return True

def _activo_devolver(self, prestamo):
    prestamo.fecha_devolucion = date.today()
    prestamo._cambiar_estado(EstadoDevuelto())
    return True

def _activo_descripcion(self):
    return "Activo"


EstadoActivo = MetaEstadoPrestamo(
    "EstadoActivo",
    (EstadoPrestamo,),
    {
        "__module__": __name__,
        "esta_activo": _activo_esta_activo,
        "devolver": _activo_devolver,
        "descripcion": _activo_descripcion
    }
)


def _devuelto_esta_activo(self):
    return False

def _devuelto_devolver(self, prestamo):
    return False

def _devuelto_descripcion(self):
    return "Devuelto"


EstadoDevuelto = MetaEstadoPrestamo(
    "EstadoDevuelto",
    (EstadoPrestamo,),
    {
        "__module__": __name__,
        "esta_activo": _devuelto_esta_activo,
        "devolver": _devuelto_devolver,
        "descripcion": _devuelto_descripcion
    }
)


class Prestamo():

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.__estado = EstadoActivo()

    def esta_activo(self):
        return self.__estado.esta_activo()

    def registrar_devolucion(self):
        return self.__estado.devolver(self)

    def obtener_estado(self):
        return self.__estado.descripcion()

    def _cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def __str__(self):
        devolucion = "Pendiente" if self.fecha_devolucion is None else self.fecha_devolucion

        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
            f"Fecha de préstamo: {self.fecha_prestamo} | "
            f"Fecha de devolución: {devolucion} | "
            f"Estado: {self.obtener_estado()}"
        )
