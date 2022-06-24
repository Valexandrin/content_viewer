import os

from pydantic import BaseModel


class Server(BaseModel):
    host: str
    port: int


class DataList(BaseModel):
    endpoint: str


class AppConfig(BaseModel):
    server: Server
    images_data: DataList


def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    endpoint = os.environ['CSV_PATH']
    return AppConfig(
        server=Server(port=app_port, host=app_host),
        images_data=DataList(endpoint=endpoint),
    )


config = load_from_env()
