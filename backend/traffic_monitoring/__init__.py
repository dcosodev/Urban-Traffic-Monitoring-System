from __future__ import absolute_import, unicode_literals

# Esto asegurará que Celery siempre se importe cuando Django arranca
from .celery import app as celery_app

__all__ = ('celery_app',)
