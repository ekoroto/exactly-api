from core.services import MinioClient
from ..schemas import ImageWithUrlSchema
from ..storages import ImageStorage


class ImageCases:
    def __init__(self, image_storage: ImageStorage, minio_client: MinioClient) -> None:
        self.image_storage = image_storage
        self.minio_client = minio_client

    async def get_images(self) -> list[ImageWithUrlSchema]:
        images = await self.image_storage.get_list()

        return [ImageWithUrlSchema(**image.dict(), url=self._get_bucket_url(image.file_path)) for image in images]

    def _get_bucket_url(self, file_path: str) -> str:
        return self.minio_client.get_image_url(file_path)
