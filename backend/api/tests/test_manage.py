from django.test import SimpleTestCase
from django.core.management import call_command

class ManageTestCase(SimpleTestCase):
    def test_manage_py(self):
        try:
            call_command('check')
        except Exception as e:
            self.fail(f"manage.py contiene un error: {e}")
