from django.test import SimpleTestCase
from importlib import import_module

class ASGITestCase(SimpleTestCase):
    def test_asgi_import(self):
        try:
            import_module('traffic_monitoring.asgi')
        except Exception as e:
            self.fail(f"Import de ASGI falló: {e}")

class WSGITestCase(SimpleTestCase):
    def test_wsgi_import(self):
        try:
            import_module('traffic_monitoring.wsgi')
        except Exception as e:
            self.fail(f"Import de WSGI falló: {e}")
