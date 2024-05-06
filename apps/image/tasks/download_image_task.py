from dependency_injector.wiring import inject, Provide

from celery_app import app
from core.helpers import run_coroutine
from ..services import DownloadImageService


@app.task(name='download_image')
@inject
def download_image(download_image_service: DownloadImageService = Provide['download_image_service']):
    run_coroutine(download_image_service.get_and_save_image())
