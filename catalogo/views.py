from django.shortcuts import render
from .models import Bebida, Pedido, Cliente, PedidoDetalle
from django.db.models import Sum

#Create your views here.

def index(request):

    # Genera contadores de algunos de los objetos principales
    num_bebidas = Bebida.objects.all().count()
    num_pedidos = Pedido.objects.all().count()
    # Bebidas disponibles (stock > 0)
    num_bebidas_disponibles = Bebida.objects.all().aggregate(Sum('stock'))
    #num_bebidas_disponibles = Bebida.objects.filter(stock__gt=0).count()

   
 # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_bebidas':num_bebidas, 'num_pedidos':num_pedidos, 'num_bebidas_disponibles':num_bebidas_disponibles},
    )