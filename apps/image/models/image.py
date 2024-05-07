from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db import Base
from ..types import ImageTypes

class Image(Base):
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[ImageTypes] = mapped_column(server_default=ImageTypes.NOT_RECOGNIZED)

    created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), server_default=func.now())
