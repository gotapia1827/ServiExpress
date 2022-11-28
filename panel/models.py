from django.db import models

# Create your models here.

class Usuarios(models.Model) :
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(null=False)
    f_crear = models.DateField(null=False)
    tipouser = models.CharField(max_length=30, null=False)
    class Meta:
        db_table = 'usuarios'

class Agenda(models.Model) :
    id = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=30, null=False)
    marca = models.CharField(max_length=30, null=False)
    patente = models.CharField(max_length=30, null=False)
    chasis = models.IntegerField(null=False)
    f_ingreso = models.DateField(null=False)
    falla = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=30, null=False)    
    class Meta:
        db_table = 'agenda'
        