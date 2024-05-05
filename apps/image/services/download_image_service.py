import base64
import requests

from datetime import datetime

from ..schemas import ImageForCreateSchema
from ..storages import ImageStorage
from ..exceptions import DownloadImageException
from ..types import ImageTypes

from settings import EXACTLY_RETRIEVE_IMAGE_URL, PUBLIC_IMAGES_PATH


class DownloadImageService:
    def __init__(self, image_storage: ImageStorage) -> None:
        self.image_storage = image_storage

    async def get_and_save_image(self):
        content = self._get_image()
        file_path = self._create_file_from_bytes(content)
        #TODO: identify is it dog or cat
        image_type = ImageTypes.DOG
        await self.image_storage.create(ImageForCreateSchema(file_path=file_path, type=image_type))

    @staticmethod
    def _get_image() -> bytes:
        custom_header = {'Accept-Encoding': 'gzip'}
        response = requests.post(EXACTLY_RETRIEVE_IMAGE_URL, headers=custom_header)

        if not response.status_code == 200:
            raise DownloadImageException()

        return response.content

    @staticmethod
    def _create_file_from_bytes(content: bytes) -> str:
        # We believe that this is a test demo and it is quite simple to store files locally without using the clouds.
        decoded_content = base64.b64decode(content)
        filename = f'{PUBLIC_IMAGES_PATH}/image_{int(datetime.now().timestamp())}.png'

        with open(filename, 'wb') as f:
            f.write(decoded_content)

        return filename
