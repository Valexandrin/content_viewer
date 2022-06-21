import csv
import os


class Image:
    def __init__(self, url: str, shows: int, categories: set) -> None:
        self.url = url
        self.amount_of_shows = shows
        self.categories = categories


def create_list(path: str):
    img_list = []
    total_shows = 0
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            image_url, amount_of_shows, *categories = row
            amount_of_shows = int(amount_of_shows)
            categories = set(categories)
            img_list.append(Image(image_url, amount_of_shows, categories))
            total_shows += amount_of_shows

    return img_list, total_shows


images_list, total_shows = create_list(os.environ['CSV_PATH'])

