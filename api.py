import settings
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.image.image_router import router as image_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(image_router)

if __name__ == "__main__":
    uvicorn.run("api:app", host=settings.HOST, port=settings.PORT, reload=settings.HOT_RELOAD)
