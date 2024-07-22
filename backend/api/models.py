from django.db import models
import uuid

class TrafficFlow(models.Model):
    """
    Modelo que representa el flujo de tráfico en una calle específica en un momento dado.

    Atributos:
        street (CharField): Nombre de la calle.
        timestamp (DateTimeField): Fecha y hora del registro del flujo de tráfico.
        vehicle_count (IntegerField): Número de vehículos registrados.
    """
    street = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    vehicle_count = models.IntegerField()

    def __str__(self):
        return f"{self.street} - {self.timestamp}"

class TrafficIncident(models.Model):
    """
    Modelo que representa un incidente de tráfico en una calle específica en un momento dado.

    Atributos:
        incident_id (CharField): Identificador único del incidente.
        street (CharField): Nombre de la calle donde ocurrió el incidente.
        timestamp (DateTimeField): Fecha y hora del incidente.
        description (TextField): Descripción del incidente.
        response_time (IntegerField): Tiempo de respuesta en minutos.
    """
    incident_id = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10])
    street = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    description = models.TextField()
    response_time = models.IntegerField()

    def __str__(self):
        return f"Incident {self.incident_id} - {self.street}"

class TrafficSensor(models.Model):
    """
    Modelo que representa los datos de un sensor de tráfico en una intersección específica en un momento dado.

    Atributos:
        sensor_id (CharField): Identificador único del sensor.
        intersection (CharField): Nombre de la intersección donde se encuentra el sensor.
        timestamp (DateTimeField): Fecha y hora del registro del sensor.
        vehicles_detected (IntegerField): Número de vehículos detectados.
        traffic_light_status (CharField): Estado del semáforo (por ejemplo, "red", "green", "yellow").
    """
    sensor_id = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10])
    intersection = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    vehicles_detected = models.IntegerField()
    traffic_light_status = models.CharField(max_length=10)

    def __str__(self):
        return f"Sensor {self.sensor_id} - {self.intersection}"
