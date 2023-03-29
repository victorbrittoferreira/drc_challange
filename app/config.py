import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class ApiConfig:
    # API_KEY = os.environ.get("API_KEY")

    PRODUCTION = os.environ.get("PRODUCTION")
    RELOAD_API = bool(not PRODUCTION)

    SERVER_HOST = os.environ.get("SERVER_HOST") or "localhost"
    SERVER_PORT = int(os.environ.get("SERVER_PORT") or 8000)

    # if PRODUCTION:
    #     sentry_sdk.init(
    #         dsn=SENTRY_DSN,
    #         traces_sample_rate=1.0,
    #     )
    #     LOGGER = logging.getLogger("produc_logger")
    # else:
    #     LOGGER = logging.getLogger("root")
