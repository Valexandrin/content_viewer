import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Image:
    def __init__(self, url: str, shows: int, categories: set) -> None:
        self.url = url
        self.amount_of_shows = shows
        self.categories = categories
        self.name = Path(self.url).name

    def __str__(self) -> str:
        return 'Image, {name}'.format(
            name=self.name,
        )


def create_list(path: str) -> tuple[list, set]:
    img_list = []
    avaliable_categories: set[str] = set()
    with open(path, 'r') as csvfile:
        for row in csv.reader(csvfile, delimiter=';'):
            try:
                image = get_instance(row)
            except ValueError:
                continue
            img_list.append(image)
            avaliable_categories |= image.categories

    img_list.sort(key=lambda img: img.amount_of_shows, reverse=True)

    logger.info(' {amount} images loaded'.format(amount=len(img_list)))
    return img_list, avaliable_categories


def get_instance(img_data):
    image_url, amount_of_shows, *categories = img_data
    return Image(image_url, int(amount_of_shows), set(categories))
