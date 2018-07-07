from django.db import models
from inventario.models import Medicamento
#from apps.clientes.models import Cliente
from django.db.models import signals

class Factura(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    cliente = models.CharField(max_length=10)
    medicamento = models.ManyToManyField(Medicamento, through='Detalle_Facturas')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo


class Detalle_Facturas(models.Model):
    Factura=models.ForeignKey(Factura,null=True, on_delete=models.SET_NULL)
    medicamento=models.ForeignKey(Medicamento,null=True, on_delete=models.SET_NULL)
    cantidad=models.IntegerField()

    def precioventa(self):
        return (self.medicamento.precio_venta)

    def total_venta(self):
        total=(self.medicamento.precio_venta*self.cantidad)
        return total

    def totalt(self):
        detalles = Detalle_Facturas.objects.filter(medicamento=self.pk)
        total = 1
        for detalle in detalles:
            suma = self.medicamento.precio_venta * self.cantidad
            total = total + suma
            return total

    def __str__(self):
        return self.medicamento.nombre


def update_stock(sender, instance, **kwargs):
    instance.medicamento.stock -= instance.cantidad
    instance.medicamento.save()

# register the signal
signals.post_save.connect(update_stock, sender=Detalle_Facturas, dispatch_uid="update_stock_count")
