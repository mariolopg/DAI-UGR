# Create your models here.
# recetas/models.py
from django.db import models
import os
  
class Receta(models.Model):
  nombre       = models.CharField(max_length=200)
  preparacion  = models.TextField(max_length=5000)
  
  def __str__(self):
    return self.nombre
  
class Ingrediente(models.Model):
  nombre        = models.CharField(primary_key = True, max_length=100)
  cantidad      = models.PositiveSmallIntegerField()
  unidades      = models.CharField(max_length=5)
  receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)
  
class Foto(models.Model):
  receta = models.ForeignKey(Receta, on_delete = models.CASCADE)
  foto = models.FileField(upload_to = 'fotos')

  def __str__(self):
    return os.path.basename(self.foto.name)