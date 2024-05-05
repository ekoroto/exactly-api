import dotenv
import os

from pathlib import Path


path_to_env = Path(__file__).parents[1].joinpath(".env")

dotenv.load_dotenv(dotenv_path=path_to_env)

PORT = int(os.environ.get("PORT", 8000))
HOST = os.environ.get("HOST", "0.0.0.0")
ENV = os.environ.get("ENV")

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
