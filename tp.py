"""Consigna General
Desarrollar una aplicación en Python denominada Sistema de Gestión de Biblioteca Digital. El
sistema deberá permitir administrar libros, usuarios y préstamos utilizando Programación
Orientada a Objetos.
Requerimientos Funcionales
Gestión de Libros
Datos mínimos: Título, Autor, ISBN, Año de publicación y Cantidad de páginas.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
Gestión de Usuarios
Datos mínimos: Nombre, Apellido, DNI y Correo electrónico.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
Gestión de Préstamos
Registrar préstamos, devoluciones y consultar préstamos activos.
Un libro no podrá prestarse si ya posee un préstamo activo.
Se deberá registrar fecha de préstamo y devolución.
Requerimientos Técnicos
• Implementar al menos una jerarquía de herencia.
• Implementar al menos un comportamiento polimórfico.
• Implementar al menos una relación de agregación.
• Implementar al menos una relación de composición.

• Implementar al menos un decorador propio e integrarlo dentro del sistema.
• Implementar una metaclase utilizando type o una clase derivada de type.
• Implementar al menos un patrón de diseño, debidamente justificado.
Diagrama UML
El trabajo deberá incluir un diagrama UML completo que represente: Clases Atributos Métodos
principales Relaciones de herencia Relaciones de agregación Relaciones de composición
Git y GitHub
1. Crear un repositorio para el proyecto.
2. Invitar al docente mediante el usuario compudiego.
3. Mantener un historial de commits representativo del desarrollo realizado.
4. Utilizar mensajes de commit descriptivos.
README.md
El repositorio deberá contener obligatoriamente un archivo README.md con: Título del trabajo.
Breve descripción del sistema desarrollado. Nombre y apellido de todos los integrantes del grupo.
Instrucciones para ejecutar el proyecto.
Condiciones de Entrega
La entrega se considerará realizada únicamente cuando: El repositorio se encuentre accesible
para el docente. El usuario compudiego haya sido invitado al repositorio. El código fuente se
encuentre completo. El UML se encuentre incluido en el repositorio. El archivo README.md se
encuentre correctamente confeccionado.

No se aceptarán entregas por correo electrónico, aula virtual ni archivos
comprimidos."""

class Biblioteca():
    def __init__(self):
        self.libros= []
        self.usuarios = []
    
    def agregar_l(self, objeto_libro):
        self.libros.append(objeto_libro)
    
    def agregar_u(self, objeto_usuario):
        self.usuarios.append(objeto_usuario)

class Libro():
    def __init__(self, titulo, autor, isbn, publicacion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.publicacion = publicacion
        self.paginas = paginas

class Usuarios():
    def __init__(self, nombre, apellido, dni, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo

class Prestamos():
    def prestamo(self):
        pass