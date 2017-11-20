# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class inv_marcas(models.Model):
    _DATABASE = "dbmssql"
    inv_marca_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    siglas = models.CharField(max_length=20)
    tipo = models.CharField(max_length=2)

    class Meta:
        managed = False

class inv_modelos(models.Model):
    _DATABASE = "dbmssql"
    inv_modelo_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    marca = models.ForeignKey(inv_marcas)
    hw_parte = models.CharField(max_length=100)
    inv_catalogo_hardware_id = models.IntegerField()

    class Meta:
        managed = False

class siga_dependencias(models.Model):
    _DATABASE = "dbmssql"
    dependenciasid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=15)

    class Meta:
        managed = False

class siga_unidadesorganicas(models.Model):
    _DATABASE = "dbmssql"
    unidadorganicaid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    dependenciasid = models.IntegerField()
    dependencia = models.CharField(max_length=100)
    noesunidad = models.BooleanField(default=False)

    class Meta:
        managed = False

class siga_usuarios(models.Model):
    _DATABASE = "dbmssql"
    usuariosid = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=300)
    dni = models.CharField(max_length=8)

    class Meta:
        managed = False


