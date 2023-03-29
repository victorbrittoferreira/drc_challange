import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class ApiConfig:
    PRODUCTION = os.environ.get("PRODUCTION")
    RELOAD_API = bool(not PRODUCTION)

    SERVER_HOST = os.environ.get("SERVER_HOST") or "localhost"
    SERVER_PORT = int(os.environ.get("SERVER_PORT") or 8000)
    WORKERS = int(os.environ.get("WORKERS") or 1)
    LOG_LEVEL = os.environ.get("LOG_LEVEL") or "info"
