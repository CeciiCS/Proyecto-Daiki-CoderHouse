from django.db import models

# Create your models here.

class Manga(models.Model):

    def __str__(self):
        return f"nombre: {self.nombre} - género: {self.genero} - autor: {self.autor} - año de lanzamiento: {self.anio_lanzamiento} - cantidad de tomos: {self.cantidad_tomos}"

    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=20)
    autor = models.CharField(max_length=30)
    anio_lanzamiento = models.IntegerField()
    cantidad_tomos = models.IntegerField()

    class Meta:
        verbose_name = "Manga"
        verbose_name_plural = "Mangas"

class Anime(models.Model):

    def __str__(self):
        return f"nombre: {self.nombre} - estado de emisión: {self.estado_emision} - estudio: {self.estudio} - cantidad de temporadas: {self.temporadas}"

    nombre = models.CharField(max_length=40)
    estado_emision = models.CharField(max_length=20)
    estudio = models.CharField(max_length=30)
    temporadas = models.IntegerField()

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"

class Pelicula(models.Model):

    def __str__(self):
        return f"nombre: {self.nombre} - estudio: {self.estudio} - fecha de estreno: {self.fecha_estreno} - duración en minutos: {self.duracion}"

    nombre = models.CharField(max_length=40)
    estudio = models.CharField(max_length=30)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()

    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"