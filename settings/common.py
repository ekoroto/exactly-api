import dotenv
import os

from celery.schedules import crontab
from pathlib import Path


path_to_env = Path(__file__).parents[1].joinpath('.env')

dotenv.load_dotenv(dotenv_path=path_to_env)

PORT = int(os.environ.get('PORT', 8000))
HOST = os.environ.get('HOST', '0.0.0.0')
ENV = os.environ.get('ENV')

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = int(os.environ.get('DB_PORT', 5432))

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERYBEAT_SCHEDULE = {
    'download-image': {
        'task': 'download_image',
        'schedule': crontab(minute='*/2'),  # Execute every 2 minutes.
    }
}

REDIS_URL = os.environ.get('REDIS_URL')
REDIS_USERNAME = os.environ.get('REDIS_USERNAME')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

EXACTLY_RETRIEVE_IMAGE_URL = os.environ.get('EXACTLY_RETRIEVE_IMAGE_URL', '')
PUBLIC_IMAGES_PATH=os.environ.get('PUBLIC_IMAGES_PATH')
