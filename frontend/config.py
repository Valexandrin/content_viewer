import os

from pydantic import BaseModel
from frontend.data.data_processing import create_list


class Server(BaseModel):
    host: str
    port: int


class DataList(BaseModel):
    images: list
    shows: int
    categories: set

class AppConfig(BaseModel):
    server: Server
    data: DataList



def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    images_list, total_shows, all_categories = create_list(os.environ['CSV_PATH'])
    return AppConfig(
        server=Server(port=app_port, host=app_host),
        data=DataList(images=images_list, shows=total_shows, categories=all_categories),
    )


config = load_from_env()
