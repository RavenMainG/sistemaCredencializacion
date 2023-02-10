from django.db import models

# Create your models here.

class Alumno(models.Model):
    
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    tipo_alumno = models.CharField(max_length=14)
    carrera = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    num_telefono = models.CharField(max_length=10)
    fecha_nac = models.DateField()
    correo = models.CharField(max_length=50)
    token = models.TextField()
    activo = models.BooleanField(default=False)
    

    
    
    
    