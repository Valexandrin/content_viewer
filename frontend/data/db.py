import csv
import os


class Image:
    def __init__(self, url, shows) -> None:
        self.url = url
        self.amount_of_shows = shows


def create_dict(path):
    config = {}
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            image_url, amount_of_shows, *categories = row
            img = Image(image_url, amount_of_shows)
            for category in categories:
                if not category in config.keys():
                    config[category] = []
                config[category].append(img)
    return config


db = create_dict(os.environ['CSV_PATH'])
