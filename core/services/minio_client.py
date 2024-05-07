import io
import urllib3

from datetime import timedelta
from minio import Minio

from settings import FILE_STORAGE_MINIO_URL, FILE_STORAGE_ACCESS_KEY, FILE_STORAGE_SECREY_KEY, \
                     FILE_STORAGE_MINIO_BUCKET_NAME, FILE_STORAGE_MINIO_EXPIRATION_HOURS

from ..exceptions import AddImageMinioException, GetImageURLMinioException


class MinioClient():
    """
    Client that works with Minio Storage. Can be injected into FileStorage instance
    """
    def __init__(self):
        self.client = Minio(
            FILE_STORAGE_MINIO_URL,
            access_key=FILE_STORAGE_ACCESS_KEY,
            secret_key=FILE_STORAGE_SECREY_KEY,
            secure=False,
            http_client=urllib3.PoolManager(cert_reqs='CERT_NONE',)
        )
        self._bucket_name = FILE_STORAGE_MINIO_BUCKET_NAME

    def upload_image(self, image_name: str, image_data: bytes) -> None:
        try:
            if not self.client.bucket_exists(self._bucket_name):
                self.client.make_bucket(self._bucket_name)

            self.client.put_object(
                self._bucket_name,
                image_name,
                io.BytesIO(image_data),
                content_type="image/png",
                length=len(image_data),
            )
        except Exception:
            raise AddImageMinioException()

    def get_image_url(self, image_name: str) -> str:
        try:
            presigned_url = self.client.presigned_get_object(
                self._bucket_name, image_name, expires=timedelta(hours=2)
            )

            return presigned_url
        except Exception:
            raise GetImageURLMinioException()
