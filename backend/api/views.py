from rest_framework import generics
from .models import TrafficFlow, TrafficIncident, TrafficSensor
from .serializers import TrafficFlowSerializer, TrafficIncidentSerializer, TrafficSensorSerializer

class TrafficFlowListCreate(generics.ListCreateAPIView):
    """
    get:
    Retorna una lista de todos los flujos de tráfico existentes.

    post:
    Crea una nueva instancia de flujo de tráfico.
    """
    queryset = TrafficFlow.objects.all()
    serializer_class = TrafficFlowSerializer

class TrafficFlowDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retorna una instancia específica de flujo de tráfico.

    put:
    Actualiza una instancia específica de flujo de tráfico.

    delete:
    Elimina una instancia específica de flujo de tráfico.
    """
    queryset = TrafficFlow.objects.all()
    serializer_class = TrafficFlowSerializer

class TrafficIncidentListCreate(generics.ListCreateAPIView):
    """
    get:
    Retorna una lista de todos los incidentes de tráfico existentes.

    post:
    Crea una nueva instancia de incidente de tráfico.
    """
    queryset = TrafficIncident.objects.all()
    serializer_class = TrafficIncidentSerializer

class TrafficIncidentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retorna una instancia específica de incidente de tráfico.

    put:
    Actualiza una instancia específica de incidente de tráfico.

    delete:
    Elimina una instancia específica de incidente de tráfico.
    """
    queryset = TrafficIncident.objects.all()
    serializer_class = TrafficIncidentSerializer

class TrafficSensorListCreate(generics.ListCreateAPIView):
    """
    get:
    Retorna una lista de todos los sensores de tráfico existentes.

    post:
    Crea una nueva instancia de sensor de tráfico.
    """
    queryset = TrafficSensor.objects.all()
    serializer_class = TrafficSensorSerializer

class TrafficSensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retorna una instancia específica de sensor de tráfico.

    put:
    Actualiza una instancia específica de sensor de tráfico.

    delete:
    Elimina una instancia específica de sensor de tráfico.
    """
    queryset = TrafficSensor.objects.all()
    serializer_class = TrafficSensorSerializer
