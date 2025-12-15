class Libro:
    def __init__(self,titulo,autor,año,disponible):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.disponible=disponible
    def prestar(self):
        if self.disponible=="true":
            print("Libro prestado exitosamente!")
            self.disponible="false"
        else:
            print("Libro no disponible, debe ser devuelto")
    def devolver(self):
        if self.disponible=="false":
            print("Libro devuelto exitosamente!")
        else:
            print("Error: el libro esta disponible")
    def mostrarDatos(self):
        print (f("Titulo: {self.titulo},\n"))

class biblioteca:
    def __init__(self):
        self.libros=[Libro("Harry Potter","J.K.Rolling",1997,"True"),
                     Libro("Yo antes de ti","JoJo Moyes",2012, "True")]
    def agregarLibro(self,Libro):
        self.libros.append(Libro)
    def librosDisponibles(self):
        for i in self.libros:
            if(i.self.disponible()=="true"):
                print(i)
