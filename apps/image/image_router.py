from dependency_injector.wiring import inject, Provide
from fastapi import status, Depends, APIRouter

from .cases import ImageCases
from .schemas import ImageWithUrlSchema


__all__ = ('router',)

router = APIRouter(prefix='/images')


@router.get('/', status_code=status.HTTP_200_OK)
@inject
async def get_images(
    image_cases: ImageCases = Depends(Provide['image_cases'])
) -> list[ImageWithUrlSchema]:
    return await image_cases.get_images()
