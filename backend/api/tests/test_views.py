from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework import status
from api.models import TrafficFlow, TrafficIncident, TrafficSensor
from django.urls import reverse

class TrafficFlowAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.traffic_flow_data = {'street': 'Main St', 'timestamp': '2024-01-01T00:00:00Z', 'vehicle_count': 100}
        self.response = self.client.post('/api/trafficflow/', self.traffic_flow_data, format='json')

    def test_api_can_create_a_traffic_flow(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_traffic_flow(self):
        traffic_flow = TrafficFlow.objects.get(street='Main St')
        response = self.client.get(f'/api/trafficflow/{traffic_flow.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, traffic_flow.street)

class TrafficIncidentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.traffic_incident_data = {'incident_id': 'INC001', 'street': 'Main St', 'timestamp': '2024-01-01T00:00:00Z', 'description': 'Accidente', 'response_time': 15}
        self.response = self.client.post('/api/trafficincident/', self.traffic_incident_data, format='json')

    def test_api_can_create_a_traffic_incident(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_traffic_incident(self):
        incident = TrafficIncident.objects.get(incident_id='INC001')
        response = self.client.get(f'/api/trafficincident/{incident.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, incident.description)

class TrafficSensorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.traffic_sensor_data = {'sensor_id': 'SEN001', 'intersection': '1st & Main', 'timestamp': '2024-01-01T00:00:00Z', 'vehicles_detected': 100, 'traffic_light_status': 'green'}
        self.response = self.client.post('/api/trafficsensor/', self.traffic_sensor_data, format='json')

    def test_api_can_create_a_traffic_sensor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_traffic_sensor(self):
        sensor = TrafficSensor.objects.get(sensor_id='SEN001')
        response = self.client.get(f'/api/trafficsensor/{sensor.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, sensor.intersection)

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Urban Traffic Monitoring System")
