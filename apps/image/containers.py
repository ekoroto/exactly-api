from dependency_injector import containers, providers

from .services import DownloadImageService
from .storages import ImageStorage


class Container(containers.DeclarativeContainer):
    image_storage = providers.Singleton(ImageStorage)
    download_image_service = providers.Singleton(DownloadImageService, image_storage)
