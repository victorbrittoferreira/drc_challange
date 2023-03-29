from config import ApiConfig


def test_api_config():
    assert hasattr(ApiConfig, "PRODUCTION")
    assert hasattr(ApiConfig, "RELOAD_API")
    assert hasattr(ApiConfig, "SERVER_HOST")
    assert hasattr(ApiConfig, "SERVER_PORT")
    assert hasattr(ApiConfig, "WORKERS")
    assert hasattr(ApiConfig, "LOG_LEVEL")
