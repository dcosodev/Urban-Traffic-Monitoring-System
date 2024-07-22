from django.test import TestCase
from api.models import TrafficFlow, TrafficIncident, TrafficSensor

class TrafficFlowTestCase(TestCase):
    def setUp(self):
        self.flow = TrafficFlow.objects.create(street="Main St", timestamp="2024-01-01T00:00:00Z", vehicle_count=100)

    def test_traffic_flow_creation(self):
        flow = TrafficFlow.objects.get(street="Main St")
        self.assertEqual(flow.vehicle_count, 100)
        self.assertEqual(flow.street, "Main St")

    def test_traffic_flow_str(self):
        # Ajusta el formato del timestamp para coincidir con el esperado en la prueba
        self.assertEqual(str(self.flow), "Main St - 2024-01-01T00:00:00Z")

class TrafficIncidentTestCase(TestCase):
    def setUp(self):
        self.incident = TrafficIncident.objects.create(incident_id="INC001", street="Main St", timestamp="2024-01-01T00:00:00Z", description="Accidente", response_time=15)

    def test_traffic_incident_creation(self):
        incident = TrafficIncident.objects.get(incident_id="INC001")
        self.assertEqual(incident.response_time, 15)
        self.assertEqual(incident.description, "Accidente")

    def test_traffic_incident_str(self):
        self.assertEqual(str(self.incident), "Incident INC001 - Main St")

class TrafficSensorTestCase(TestCase):
    def setUp(self):
        self.sensor = TrafficSensor.objects.create(sensor_id="SEN001", intersection="1st & Main", timestamp="2024-01-01T00:00:00Z", vehicles_detected=100, traffic_light_status="green")

    def test_traffic_sensor_creation(self):
        sensor = TrafficSensor.objects.get(sensor_id="SEN001")
        self.assertEqual(sensor.traffic_light_status, "green")
        self.assertEqual(sensor.vehicles_detected, 100)

    def test_traffic_sensor_str(self):
        self.assertEqual(str(self.sensor), "Sensor SEN001 - 1st & Main")
