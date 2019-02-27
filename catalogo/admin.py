from django.contrib import admin
from .models import Bebida, Pedido, Cliente #importar los modelos

# Register your models here.

#admin.site.register(Bebida)
admin.site.register(Pedido)
admin.site.register(Cliente)

# Define the admin class
class BebidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tamanho', 'sabor', 'tipo', 'contenido_alcohol', 'precio', 'stock')
    list_filter = ('tamanho','sabor','tipo','contenido_alcohol')

# Register the admin class with the associated model
admin.site.register(Bebida, BebidaAdmin)