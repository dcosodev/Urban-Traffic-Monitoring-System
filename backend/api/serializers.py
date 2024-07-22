from rest_framework import serializers
from .models import TrafficFlow, TrafficIncident, TrafficSensor

class TrafficFlowSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TrafficFlow.
    Este serializador maneja la serialización y deserialización del modelo TrafficFlow,
    que representa el flujo de tráfico en una calle específica en un momento dado.
    """

    class Meta:
        model = TrafficFlow
        fields = '__all__'


class TrafficIncidentSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TrafficIncident.
    Este serializador maneja la serialización y deserialización del modelo TrafficIncident,
    que representa un incidente de tráfico en una calle específica en un momento dado.
    """

    class Meta:
        model = TrafficIncident
        fields = '__all__'


class TrafficSensorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TrafficSensor.
    Este serializador maneja la serialización y deserialización del modelo TrafficSensor,
    que representa los datos de un sensor de tráfico en una intersección específica en un momento dado.
    """

    class Meta:
        model = TrafficSensor
        fields = '__all__'
