import csv
import os


class Image:
    def __init__(self, url, shows) -> None:
        self.url = url
        self.amount_of_shows = shows


class Database:
    def __init__(self, path) -> None:
        self.config = self.__create_dict(path)


    def __create_dict(self, path):
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


db = Database(os.environ['CSV_PATH'])
