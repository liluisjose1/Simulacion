from django.contrib import admin

# Register your models here.

from ventas.models import Detalle_Facturas, Factura


class Detalle_FacturasInline(admin.TabularInline):
    model = Detalle_Facturas

class FacturaAdmin(admin.ModelAdmin):
    inlines = (Detalle_FacturasInline,)
    #search_fields = ('fecha', '')


admin.site.register(Factura, FacturaAdmin)
