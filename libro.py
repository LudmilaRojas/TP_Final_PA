class Libro():

    def __init__(self, titulo, autor, isbn, publicacion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.publicacion = publicacion
        self.paginas = paginas

    def set_titulo(self, nuevo):
        self.titulo = nuevo

    def set_autor(self, nuevo):
        self.autor = nuevo

    def set_isbn(self, nuevo):
        self.isbn = nuevo

    def set_publicacion(self, nuevo):
        self.publicacion = nuevo

    def set_paginas(self, nuevo):
        self.paginas = nuevo

    def __str__(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn} | "
            f"Año: {self.publicacion} | "
            f"Páginas: {self.paginas}"
        )
