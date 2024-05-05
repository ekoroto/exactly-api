from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from dependency_injector.wiring import inject, Provide

from db import start_session, DBContainer
from ..models import Image
from ..schemas import ImageForCreateSchema, ImageSchema


class ImageStorage:
    model_class = Image

    @inject
    async def create(
        self,
        image: ImageForCreateSchema,
        session: AsyncSession = Depends(Provide[DBContainer.session])
    ) -> ImageSchema:
        async with start_session(session) as session:
            image = self.model_class(**image.model_dump())
            session.add(image)
            await session.flush()

        return ImageSchema.model_validate(image)
