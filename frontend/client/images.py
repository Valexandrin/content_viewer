from frontend.config import config
from frontend.data.data_processing import create_list


class ImagesClient:
    def __init__(self, images: list, categories: set) -> None:
        self.images = images
        self.avaliable_categories = categories
        self.last_shown = None

    def get_image(self, required_categories: set):
        if not self.images:
            return None

        valid_categories = self.avaliable_categories & required_categories
        if not valid_categories:
            return None

        relevant_images = self._check_matching_request(valid_categories)
        if not relevant_images:
            return None

        resault_image = self._get_by_views(relevant_images)
        return self._get_updated_image(resault_image)

    def get_random_image(self):
        if not self.images:
            return None

        resault_image = {}
        if len(self.images) == 1:
            resault_image[self.images[0]] = 0
            return self._get_updated_image(resault_image)

        for number, _ in enumerate(self.images):
            image = self.images[number]

            if image is not self.last_shown:
                resault_image[image] = number
                return self._get_updated_image(resault_image)

    def _check_matching_request(self, requested_categories: set) -> dict:
        matched_images = {}
        for number, _ in enumerate(self.images):
            image = self.images[number]
            overlap = requested_categories & image.categories
            if overlap:
                matched_images[image] = number

        return matched_images

    def _sort_images(self, image, image_number):
        try:
            next_img = self.images[image_number + 1]
        except IndexError:
            return
        if image.amount_of_shows < next_img.amount_of_shows:
            self.images.insert(image_number + 1, self.images.pop(image_number))
            self._sort_images(image, image_number + 1)

    def _get_by_views(self, relevant_images: dict) -> dict:
        if len(relevant_images.keys()) == 1:
            return relevant_images

        resault_image = {}
        for image in relevant_images.keys():
            if image is not self.last_shown:
                number_in_list = relevant_images[image]
                resault_image[image] = number_in_list
                break
        return resault_image

    def _get_updated_image(self, image_data: dict):
        for image, image_number in image_data.items():
            image.amount_of_shows -= 1
            if image.amount_of_shows == 0:
                self.images.pop(image_number)
            else:
                self._sort_images(image, image_number)

            self.last_shown = image
            return image


images, categories = create_list(config.images_data.endpoint)
image_client = ImagesClient(images, categories)
