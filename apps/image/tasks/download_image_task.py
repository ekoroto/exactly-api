import asyncio

from dependency_injector.wiring import inject, Provide

from celery_app import app

from ..services import DownloadImageService


@app.task(name='download_image')
@inject
def download_image(download_image_service: DownloadImageService = Provide['download_image_service']):
    asyncio.run(download_image_service.get_and_save_image())
