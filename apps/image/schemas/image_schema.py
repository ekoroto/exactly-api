from pydantic import BaseModel

from ..types import ImageTypes


class ImageForCreateSchema(BaseModel):
    file_path: str
    type: ImageTypes


class ImageSchema(ImageForCreateSchema):
    id: int

    class Config:
        from_attributes = True
