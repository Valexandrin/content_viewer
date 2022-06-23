import csv
from pathlib import Path
import logging


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
    avaliable_categories = set()
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            try:
                image_url, amount_of_shows, *categories = row
                amount_of_shows = int(amount_of_shows)
                categories = set(categories)
                img_list.append(Image(image_url, amount_of_shows, categories))
                avaliable_categories |= categories
            except:
                continue

    img_list.sort(key=lambda item: item.amount_of_shows, reverse=True)

    logger.info(' {} images loaded'.format(len(img_list)))
    return img_list, avaliable_categories
