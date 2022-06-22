from frontend.config import config
from random import choice


class ImagesClient:
    def __init__(self) -> None:
        self.images_shown = 0
        self.avaliable_shows = config.data.shows
        self.images = set(config.data.images)
        self.avaliable_categories = config.data.categories
        self.last_shown = None

    def __check_matching_request(self, requested_categories: set) -> dict:
        matched_images = {}
        for image in self.images:
            overlap = len(requested_categories & image.categories)
            if overlap:
                matched_images[image] = overlap
        return matched_images

    def __category_validation(self, categories: set) -> set:
        return self.avaliable_categories & categories

    def __get_resault_image(self, relevant_images: dict.keys):
        for image in relevant_images:
            if len(relevant_images) == 1:
                return image
            if not self.__match_by_shows(image):
                print('Here')
                continue
            return image

    def __match_by_shows(self, image):
        if image is self.last_shown:
            return False
        if image.amount_of_shows < self.avaliable_shows:
            return True

    def get_image(self, required_categories: set):
        validated_categories = self.__category_validation(required_categories)
        if not validated_categories:
            return None

        relevant_images = self.__check_matching_request(validated_categories)
        if not relevant_images:
            return None

        relevant_images = dict(
            sorted(relevant_images.items(), key=lambda item: item[1], reverse=True)
        )
        resault_image = self.__get_resault_image(relevant_images.keys())
        resault_image.amount_of_shows -= 1

        if resault_image.amount_of_shows == 0:
            self.images.discard(resault_image)

        self.last_shown = resault_image
        self.images_shown += 1

        return resault_image

    def get_random_image(self):
        images = list(self.images)
        image = choice(images)
        while not self.__match_by_shows(image):
            image = choice(images)

        return image
