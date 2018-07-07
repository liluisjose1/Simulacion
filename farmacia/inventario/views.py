from django.shortcuts import render
from django.utils import timezone
from .models import Categoria,Medicamento
from ventas.models import Factura,Detalle_Facturas
from django.shortcuts import redirect


# Create your views here.
from django.shortcuts import render, get_object_or_404
def index(request):
    """
    View function for home page of site.
    """
    # cantidad de objetos del modelo post
    categoras=Categoria.objects.all()
    medicamentos=Medicamento.objects.all()
    factura=Factura.objects.all()
    d_factura=Detalle_Facturas.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_cat':categoras,'num_med':medicamentos,'fact':factura,'d_fac':d_factura},
    )
