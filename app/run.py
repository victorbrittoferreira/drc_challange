import uvicorn

from config import ApiConfig
from src.api.factory import create_api

api = create_api()

if __name__ == "__main__":
    # logging.basicConfig(level="DEBUG")
    uvicorn.run(
        "run:api",
        # host=ApiConfig.SERVER_HOST,
        host="0.0.0.0",
        # port=ApiConfig.SERVER_PORT,
        port=5000,
        reload=ApiConfig.RELOAD_API,
        log_level="debug",
        workers=1,
    )
