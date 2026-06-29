## Sistema de Gestión de Biblioteca Digital

## Descripción

Sistema desarrollado en Python que permite administrar libros, usuarios y préstamos de una biblioteca digital. Implementa los principios de la Programación Orientada a Objetos, incluyendo herencia, polimorfismo, composición, agregación, decoradores, metaclases y el patrón de diseño State.

## Integrantes

* Ludmila Rojas
* Ludmila Rios
* Catalina Ballejos

## Estructura del proyecto

    ├── biblioteca.py            # Clase principal que gestiona libros, usuarios y préstamos
    ├── libro.py                 # Clase Libro con sus atributos y métodos
    ├── usuario.py               # Clase Usuario con sus atributos y métodos
    ├── requerimientos_tecnicos.py  # Decorador, metaclase, estados y clase Prestamo
    ├── invocaciones.py          # Script de ejemplo con casos de uso del sistema
    └── uml_biblioteca_digital_limpio.png  # Diagrama UML del sistema
    
## Justificación para el patrón de diseño State

Se implementó el patrón State para modelar el ciclo de vida de un préstamo. Un préstamo puede estar en dos estados: activo o devuelto, y su comportamiento varía según el estado en que se encuentre. En lugar de manejar esa lógica con condicionales dentro de la clase Prestamo, cada estado se representa con su propia clase (EstadoActivo y EstadoDevuelto), ambas construidas a partir de EstadoPrestamo. Esto permite que Prestamo delegue las operaciones a su estado actual sin necesidad de saber cuál es, lo que hace el código más fácil de mantener y extender ante nuevos estados futuros.


## Instrucciones para ejecutar el proyecto

### Requisitos previos

* Python 3.8 o superior instalado.
* No se requieren dependencias externas (solo módulos de la biblioteca estándar).

### Pasos

1. Clonar el repositorio:
  
   git clone https://github.com/LudmilaRojas/TP_Final_PA
   cd TP_Final_PA
  
2. Ejecutar el script de ejemplo:
  
      python invocaciones.py
  
  Esto demostrará el flujo completo del sistema: alta de libros y usuarios, registro de préstamos, devoluciones y consulta de registros de auditoría.
  
3. Para integrar el sistema en otro proyecto, importar las clases necesarias:
  
      from libro import Libro
      from usuario import Usuario
      from biblioteca import Biblioteca
