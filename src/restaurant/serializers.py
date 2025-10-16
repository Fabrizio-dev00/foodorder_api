from rest_framework import serializers
from .models import Plato, Pedido

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria']


class PedidoReadSerializer(serializers.ModelSerializer):
    platos = PlatoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos']


class PedidoWriteSerializer(serializers.ModelSerializer):
    platos = serializers.PrimaryKeyRelatedField(queryset=Plato.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'estado', 'platos']

    def _calcular_total(self, platos_qs):
        total = sum([p.precio for p in platos_qs])
        return total

    def create(self, validated_data):
        platos = validated_data.pop('platos', [])
        pedido = Pedido.objects.create(**validated_data)
        pedido.platos.set(platos)
        pedido.total = self._calcular_total(platos)
        pedido.save()
        return pedido

    def update(self, instance, validated_data):
        platos = validated_data.pop('platos', None)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()
        if platos is not None:
            instance.platos.set(platos)
            instance.total = self._calcular_total(platos)
            instance.save()
        return instance
