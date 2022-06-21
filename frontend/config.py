import os

from pydantic import BaseModel
from frontend.data.db import db


class Server(BaseModel):
    host: str
    port: int


class AppConfig(BaseModel):
    server: Server



def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    return AppConfig(
        server=Server(port=app_port, host=app_host),
    )


config = load_from_env()
