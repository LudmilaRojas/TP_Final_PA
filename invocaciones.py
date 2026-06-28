from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


biblioteca = Biblioteca()

l1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", 1967, 417)
l2 = Libro("El aleph", "Jorge Luis Borges", "978-950-731-080-5", 1949, 180)

biblioteca.agregar_l(l1)
biblioteca.agregar_l(l2)

u1 = Usuario("Ana", "López", "30000001", "ana@mail.com")
u2 = Usuario("Carlos", "Pérez", "30000002", "carlos@mail.com")

biblioteca.agregar_u(u1)
biblioteca.agregar_u(u2)

print("=== Libros ===")
for libro in biblioteca.listar_libros():
    print(libro)

print("\n=== Usuarios ===")
for usuario in biblioteca.listar_usuarios():
    print(usuario)

print("\n=== Préstamo ===")
resultado = biblioteca.registrar_prestamo("978-0-06-088328-7", "30000001")
print(resultado)

print("\n=== Intento de préstamo duplicado ===")
resultado = biblioteca.registrar_prestamo("978-0-06-088328-7", "30000002")
print(resultado)

print("\n=== Préstamos activos ===")
for p in biblioteca.obtener_prestamos_activos():
    print(p)

print("\n=== Devolución ===")
resultado = biblioteca.registrar_devolucion("978-0-06-088328-7")
print(resultado)

print("\n=== Préstamos activos tras devolución ===")
activos = biblioteca.obtener_prestamos_activos()
print(activos if activos else "Sin préstamos activos.")

print("\n=== Registros de auditoría ===")
for registro in biblioteca.listar_registros():
    print(registro)
