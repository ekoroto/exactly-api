import datetime

from pydantic import BaseModel

from ..types import ImageTypes


class ImageForCreateSchema(BaseModel):
    file_path: str
    type: ImageTypes = ImageTypes.DOG


class ImageSchema(ImageForCreateSchema):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True

class ImageWithUrlSchema(ImageSchema):
    url: str
