from django.contrib import admin
# Register your models here.


from inventario.models import Categoria, Medicamento,Abastecimiento


# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Abastecimiento)
class AbastecimientoAdmin(admin.ModelAdmin):
	list_display = ('medicamento','fecha_abastecimiento')

@admin.register(Medicamento)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'categoria','nombre','descripcion', 'fecha_creacion', 'precio_Compra','precio_venta', 'stock')
	search_fields = ('nombre', 'descripcion')
