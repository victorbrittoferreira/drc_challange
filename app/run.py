import uvicorn

from config import ApiConfig
from src.api.factory import create_api

api = create_api()

if __name__ == "__main__":
    uvicorn.run(
        "run:api",
        host=ApiConfig.SERVER_HOST,
        port=ApiConfig.SERVER_PORT,
        reload=ApiConfig.RELOAD_API,
        log_level=ApiConfig.LOG_LEVEL,
        workers=ApiConfig.WORKERS,
    )
