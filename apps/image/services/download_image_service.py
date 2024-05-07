import base64
import requests

from datetime import datetime

from settings import EXACTLY_RETRIEVE_IMAGE_URL
from core.exceptions import AddImageMinioException
from core.services import ImageClassificationService, MinioClient
from ..constants import BREEDS_CATALOG
from ..exceptions import DownloadImageException
from ..schemas import ImageForCreateSchema
from ..storages import ImageStorage
from ..types import ImageTypes


class DownloadImageService:
    def __init__(
        self,
        image_storage: ImageStorage,
        minio_client: MinioClient,
        image_classification_service: ImageClassificationService,
    ) -> None:
        self.image_storage = image_storage
        self.minio_client = minio_client
        self.image_classification_service = image_classification_service

    async def get_and_save_image(self):
        content = self._get_image()
        content = base64.b64decode(content)
 
        type = self.image_classification_service.predict(content, [ImageTypes.CAT, ImageTypes.DOG], BREEDS_CATALOG)

        if not type:
            type = ImageTypes.NOT_RECOGNIZED

        bucket_path = self._upload_file_to_bucket(content)

        if not bucket_path:
            raise DownloadImageException()

        await self.image_storage.create(ImageForCreateSchema(file_path=bucket_path, type=type))

    @staticmethod
    def _get_image() -> bytes:
        custom_header = {'Accept-Encoding': 'gzip'}
        response = requests.post(EXACTLY_RETRIEVE_IMAGE_URL, headers=custom_header)

        if not response.status_code == 200:
            raise DownloadImageException()

        return response.content

    def _upload_file_to_bucket(self, content: bytes) -> str | None:
        filename = f'image_{int(datetime.now().timestamp())}.png'

        try:
            self.minio_client.upload_image(filename, content)
        except AddImageMinioException:
            return None

        return filename
