import os


CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL',
    'amqp://guest@0.0.0.0:5672//'
)
