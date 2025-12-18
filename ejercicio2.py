class Libro:
    def __init__(self, titulo, autor, año, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
    
    def prestar(self):
        if self.disponible:
            print(f"Libro '{self.titulo}' prestado exitosamente")
            self.disponible = False
        else:
            print(f"Libro '{self.titulo}' no disponible, debe ser devuelto primero")
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto exitosamente")
        else:
            print(f"Error: '{self.titulo}' ya esta disponible")          
    
    def mostrarDatos(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Estado: {estado}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible=True)
        self.formato = formato
        self.tamañoMB = tamañoMB
        self.prestaciones = 0
    
    def prestar(self):
        self.prestaciones += 1
        print(f"Libro digital '{self.titulo}' prestado exitosamente (Prestamo #{self.prestaciones})")
    
    def devolver(self):
        print("Los libros digitales no necesitan devolucion")
    
    def mostrarDatos(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Formato: {self.formato}")
        print(f"Tamaño: {self.tamañoMB} MB")
        print(f"Veces prestado: {self.prestaciones}")


class Biblioteca:
    def __init__(self):
        self.libros = [
            Libro("Harry Potter", "J.K. Rowling", 1997),
            Libro("Yo antes de ti", "Jojo Moyes", 2012)
        ]
    
    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca")
    
    def listarLibros(self):
        print("\nLISTADO DE TODOS LOS LIBROS")
        for i, libro in enumerate(self.libros, 1):
            tipo = "(Digital)" if isinstance(libro, LibroDigital) else "(Fisico)"
            print(f"\n{i}. {tipo}")
            libro.mostrarDatos()
    
    def buscarPorAutor(self, autor):
        print(f"\nBuscando libros del autor: {autor}")
        encontrados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                encontrados.append(libro)
                libro.mostrarDatos()
                print()
        
        if not encontrados:
            print(f"No se encontraron libros del autor '{autor}'")
        else:
            print(f"Total encontrados: {len(encontrados)}")
    
    def prestarLibro(self, titulo):
        print(f"\nIntentando prestar: '{titulo}'")
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print(f"No se encontro el libro '{titulo}' en la biblioteca")

biblioteca1 = Biblioteca()

fisico1 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
fisico2 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967)
fisico3 = Libro("Los jefes", "Mario Vargas Llosa", 1963)

digital1 = LibroDigital("Orgullo y Prejuicio", "Jane Austen", 1813, "EPUB", 1.5)
digital2 = LibroDigital("Frankenstein", "Mary Shelley", 1818, "PDF", 3.5)

biblioteca1.agregarLibro(fisico1)
biblioteca1.agregarLibro(fisico2)
biblioteca1.agregarLibro(fisico3)
biblioteca1.agregarLibro(digital1)
biblioteca1.agregarLibro(digital2)

biblioteca1.listarLibros()
biblioteca1.prestarLibro("Don Quijote")
for i in range(5):
    biblioteca1.prestarLibro("Frankenstein")
biblioteca1.prestarLibro("Don Quijote")
biblioteca1.buscarPorAutor("Jane Austen")
biblioteca1.buscarPorAutor("Gabriel Garcia Marquez")
biblioteca1.listarLibros()
