from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.nombre} - S/{self.precio}"


class Pedido(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PREPARANDO', 'Preparando'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    platos = models.ManyToManyField(Plato, related_name='pedidos')

    def __str__(self):
        return f"Pedido {self.id} - {self.estado} - S/{self.total}"
