import base64
import requests

from datetime import datetime

from settings import EXACTLY_RETRIEVE_IMAGE_URL
from core.exceptions import AddImageMinioException
from core.services import MinioClient
from ..schemas import ImageForCreateSchema
from ..storages import ImageStorage
from ..exceptions import DownloadImageException


class DownloadImageService:
    def __init__(self, image_storage: ImageStorage, minio_client: MinioClient) -> None:
        self.image_storage = image_storage
        self.minio_client = minio_client

    async def get_and_save_image(self):
        content = self._get_image()
        bucket_path = self._upload_file_to_bucket(content)
        #TODO: identify is it dog or cat

        if not bucket_path:
            raise DownloadImageException()

        await self.image_storage.create(ImageForCreateSchema(file_path=bucket_path))

    @staticmethod
    def _get_image() -> bytes:
        custom_header = {'Accept-Encoding': 'gzip'}
        response = requests.post(EXACTLY_RETRIEVE_IMAGE_URL, headers=custom_header)

        if not response.status_code == 200:
            raise DownloadImageException()

        return response.content

    def _upload_file_to_bucket(self, content: bytes) -> str | None:
        filename = f'image_{int(datetime.now().timestamp())}.png'
        decoded_content = base64.b64decode(content)

        try:
            self.minio_client.upload_image(filename, decoded_content)
        except AddImageMinioException:
            return None

        return filename
