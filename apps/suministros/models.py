# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ..vista.models import inv_marcas, inv_modelos, siga_unidadesorganicas, siga_usuarios


class Color(models.Model):
    _DATABASE = "dbmssql"
    nombre = models.CharField(max_length=30, unique=True)
    codigo = models.CharField(max_length=7, unique=True)

    class Meta:
        managed = False

    def get_absolute_url(self):
        return ""


class Suministro(models.Model):
    _DATABASE = "dbmssql"
    tipoSum = (
        ('TN', u'Tóner'),
        ('TI', u'Tinta')
    )

    tipo = models.CharField(max_length=2, default=tipoSum[0][0])
    codigo = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=5)
    rendimiento = models.IntegerField()
    color = models.ForeignKey(Color)
    marca = models.ForeignKey(inv_marcas)

    class Meta:
        managed = False

    def get_absolute_url(self):
        return ""

    def __unicode__(self):
        return self.codigo + " - " + self.modelo

    def Tipo(self):
        result = ''
        for op in self.tipoSum:
            if op[0] == self.tipo:
                result = op[1]
                break
        return result


class ModeloCompatible(models.Model):
    _DATABASE = "dbmssql"

    modelo = models.ForeignKey(inv_modelos)
    suministro = models.ForeignKey(Suministro)
    principal = models.BooleanField(default=False)

    class Meta:
        managed = False

    def get_absolute_url(self):
        return ""

    def __unicode__(self):
        return self.suministro.codigo + " - " + self.modelo.nombre


class Requerimiento(models.Model):
    _DATABASE = "dbmssql"

    def number():
        no = Requerimiento.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    numero = models.IntegerField(('Numero'), unique=True, default=number)
    fecha = models.DateField()
    tecnico = models.ForeignKey(siga_usuarios)
    unidadorganica = models.ForeignKey(siga_unidadesorganicas)

    class Meta:
        managed = False

    def get_absolute_url(self):
        return ""

    # def __unicode__(self):
    #     return self.numero + " - " + self.unidadorganica.nombre + " - " + self.unidadorganica.dependencia


class RequerimientoDetalle(models.Model):
    _DATABASE = "dbmssql"

    requerimiento = models.ForeignKey(Requerimiento)
    cantidad = models.IntegerField()
    suministro = models.ForeignKey(Suministro)


    def get_absolute_url(self):
        return ""
    #
    # def __unicode__(self):
    #     return self.cantidad

class OrdenCompra(models.Model):
    _DATABASE = "dbmssql"

    numero = models.IntegerField()
    siaf = models.IntegerField()
    fecha = models.DateField()

    def get_absolute_url(self):
        return ""

    # def __unicode__(self):
    #     return self.numero + " - " + self.siaf

class OrdenCompraDetalle(models.Model):
    _DATABASE = "dbmssql"

    ordencompra = models.ForeignKey(OrdenCompra)
    suministro = models.ForeignKey(Suministro)
    requerimientodetalle= models.ForeignKey(RequerimientoDetalle)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad=models.IntegerField()

    def get_absolute_url(self):
        return ""

    # def __unicode__(self):
    #     return self.precio

class Pedido(models.Model):
    _DATABASE = "dbmssql"
    numero= models.IntegerField()
    fecha= models.DateField()

    def get_absolute_url(self):
        return ""
