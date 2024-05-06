import sqlalchemy as sa

from dependency_injector.wiring import Provide, inject
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic.tools import parse_obj_as

from db.orm import start_session

from ..models import Image
from ..types import ImageTypes
from ..schemas import ImageForCreateSchema, ImageSchema


class ImageStorage:
    model_class = Image

    @inject
    async def create(self, image: ImageForCreateSchema, session: AsyncSession = Provide['session']
) -> None:
        async with start_session(session):
            query = sa.insert(self.model_class).values(**image.model_dump()).returning(self.model_class)
            await session.execute(query)
            await session.commit()

    async def get_list(self, session: AsyncSession = Provide['session']) -> list[ImageSchema]:
        query = (
            sa.select(self.model_class)
            # .where(self.model_class.type == type)
            .order_by(self.model_class.created_at.desc())
            .limit(10)
        )

        async with start_session(session):
            result = (await session.execute(query)).scalars().all()

        return parse_obj_as(list[ImageSchema], result)
