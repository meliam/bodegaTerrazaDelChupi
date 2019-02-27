from django.db import models
 

#Create your models here


class Bebida(models.Model):
    
    """

    Modelo que representa una bebida.

    """


    nombre = models.CharField(max_length=200)


    tamanho = models.IntegerField(help_text="Ingresar solo números en mililitros (ml)")

    sabor = models.CharField(max_length=30)


    proveedor = models.CharField (max_length=200)


    GASEOSA = 'GASE'

    CERVEZA = 'CERV'

    WHISKY = 'WHIS'

    VODKA = 'VOD'

    TIPO_BEBIDA = (

        (GASEOSA, 'Gaseosa'),

        (CERVEZA, 'Cerveza'),

        (WHISKY, 'Whisky'),

        (VODKA, 'Vodka'),

    )


    tipo = models.CharField (max_length = 4, choices = TIPO_BEBIDA, default = GASEOSA)


    contenido_alcohol = models.IntegerField(default=0)

    precio = models.IntegerField(default=0)


    stock = models.IntegerField(default=0)


    def __str__(self):

        """

        String que representa al objeto Bebida

        """

        return self.nombre
    
 



class Cliente (models.Model):
    id_cliente = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    ruc = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):

        """

        String que representa al objeto Cliente

        """

        return self.nombre
    
 




class Pedido(models.Model):
    """

    Modelo que representa un pedido.

    """


    no_pedido = models.CharField(max_length=10, unique=True, primary_key=True)
    f_pedido = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bebidas = models.ManyToManyField('bebida', through='PedidoDetalle')
    monto_total = models.IntegerField (default=0)
    CONTADO = 'CONT'
    CREDITO = 'CRED'

    TIPO_PAGO = (

        (CONTADO, 'Contado'),

        (CREDITO, 'Crédito'),

    )
    condicion_pago = models.CharField (max_length = 4, choices = TIPO_PAGO, default = CONTADO)
    EFECTIVO = 'EFEC'
    TARJETA = 'TARJ'
    MEDIO_PAGO =(
        (EFECTIVO, 'Efectivo'),
        (TARJETA, 'Tarjeta'),
    )

    medio_pago = models.CharField (max_length = 4, choices = MEDIO_PAGO, default = EFECTIVO)

    def __str__(self):
        """

        String que representa al objeto Pedido

        """

        return self.no_pedido

class PedidoDetalle(models.Model):
   pedido = models.ForeignKey(Pedido, related_name='pedido_detalle',on_delete=models.CASCADE)
   bebida = models.ForeignKey(Bebida, related_name='pedido_detalle', on_delete=models.CASCADE)
   cantidad = models.PositiveSmallIntegerField()
