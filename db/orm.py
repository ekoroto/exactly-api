import sys

from contextlib import asynccontextmanager
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from settings import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


Base = declarative_base()

engine = create_async_engine(
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    pool_size=100,
    max_overflow=0,
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@asynccontextmanager
async def start_session(session):
    trans = None
    nested = False
    try:
        nested = session.in_transaction()
        if nested:
            trans = session.begin_nested()
        else:
            trans = session.begin()

        await trans.__aenter__()
        yield session
    finally:
        if trans:
            await trans.__aexit__(*sys.exc_info())
        if not nested:
            await session.__aexit__(*sys.exc_info())
