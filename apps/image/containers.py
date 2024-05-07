from dependency_injector import containers, providers

from core.services import ImageClassificationService, MinioClient
from .cases import ImageCases
from .services import DownloadImageService
from .storages import ImageStorage


class Container(containers.DeclarativeContainer):
    image_storage = providers.Singleton(ImageStorage)
    minio_client = providers.Singleton(MinioClient)
    image_cases = providers.Singleton(ImageCases, image_storage, minio_client)
    image_classification_service = providers.Singleton(ImageClassificationService)
    download_image_service = providers.Singleton(
        DownloadImageService, image_storage, minio_client, image_classification_service
    )
