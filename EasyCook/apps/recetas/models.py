from django.db import models

# Create your models here.
class Receta(models.Model):

    seleccionCat = (("Facil","Recetas Faciles"),("Saludable","Recetas Saludables"),("Vegetariana","Recetas Vegetarianas"),("Gourmet","Recetas Gourmet")) 

    categoria = models.CharField(max_length = 50, choices = seleccionCat, default = None)
    titulo = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 200)
    pasos = models.TextField(max_length = 500)
    imagen = models.ImageField(upload_to = 'images/')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo
