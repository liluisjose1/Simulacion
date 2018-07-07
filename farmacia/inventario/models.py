from django.db import models

# Create your models here.
from django.db.models import signals


# Create your models here.
class Categoria(models.Model):
    #codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return u'%s' % (self.nombre)

class Medicamento(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    categoria = models.ForeignKey(Categoria,null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=200, unique=True)
    fecha_creacion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_Compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

    def preeciototal(self):
        precio_total=self.precio_compra*self.stock
        return precio_total

class Abastecimiento(models.Model):
    medicamento=models.ForeignKey(Medicamento,null=True, on_delete=models.SET_NULL)
    cantidad=models.IntegerField()
    fecha_abastecimiento= models.DateField()

    def __str__(self):
        return self.medicamento.nombre


def update_stock(sender, instance, **kwargs):
    instance.medicamento.stock += instance.cantidad
    instance.medicamento.save()

# register the signal
signals.post_save.connect(update_stock, sender=Abastecimiento, dispatch_uid="update_stock_count")
