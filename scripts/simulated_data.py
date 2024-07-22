import os
import sys
import django
from faker import Faker
import random

# Asegúrate de que el directorio 'backend' esté en el PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traffic_monitoring.settings')

django.setup()

from api.models import TrafficFlow, TrafficIncident, TrafficSensor

fake = Faker()

def populate_traffic_flow(n=100):
    for _ in range(n):
        TrafficFlow.objects.create(
            street=fake.street_name(),
            timestamp=fake.date_time_this_year(),
            vehicle_count=random.randint(50, 500)
        )

def populate_incidents(n=50):
    for _ in range(n):
        TrafficIncident.objects.create(
            incident_id=fake.unique.lexify(text='INC????'),
            street=fake.street_name(),
            timestamp=fake.date_time_this_year(),
            description=fake.text(),
            response_time=random.randint(5, 60)
        )

def populate_sensors(n=50):
    for _ in range(n):
        TrafficSensor.objects.create(
            sensor_id=fake.unique.lexify(text='SEN????'),
            intersection=fake.address(),
            timestamp=fake.date_time_this_year(),
            vehicles_detected=random.randint(0, 1000),
            traffic_light_status=random.choice(['red', 'yellow', 'green'])
        )

if __name__ == "__main__":
    print("Populating traffic flow data...")
    populate_traffic_flow()
    print("Populating incidents data...")
    populate_incidents()
    print("Populating sensors data...")
    populate_sensors()
    print("Done!")
