from django.db import models

# Create your models here.

class Nota:
    def __init__(self, titulo, descripcion, importante) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.importante = importante

class Notas:
    def __init__(self) -> None:
        # notaImportante = Nota('Importante', 'asdasd', True)
        # notaNormal = Nota('Normal', 'asdasd', False)
        self.lista_notas = []

    def listar_notas(self):
        return self.lista_notas

    def buscar_notas(self, titulo):
        for n in self.lista_notas:
            if titulo == n.titulo:
                return n
        return None
    
    def crear_notas(self, nuevanota):
        resultado = self.buscar_notas(nuevanota.titulo)

        if resultado is None:
            self.lista_notas.append(nuevanota)
            return 'Nueva nota creada'
        else:
            return 'La nota ya existe'
    
    def eliminar_nota(self, titulo):
        resultado = self.buscar_notas(titulo)

        if resultado is not None and isinstance(resultado, Nota):
            self.lista_notas.remove(resultado)
            return f'Nota eliminada: {titulo}'
        return 'Nota no encontrada'

                