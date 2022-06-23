from frontend.config import config
from frontend.data.data_processing import create_list


class ImagesClient:
    def __init__(self, images: list, categories: set) -> None:
        self.images = images
        self.avaliable_categories = categories
        self.last_shown = None

    def __check_extreme(self):
        if len(self.images) == 0:
            return None
        if len(self.images) == 1:
            return self.images.pop()

    def __check_matching_request(self, requested_categories: set) -> dict:
        matched_images = {}
        for number in range(len(self.images)):
            image = self.images[number]
            overlap = requested_categories & image.categories
            if overlap:
                matched_images[image] = number
        return matched_images

    def __sort_images(self, image, image_number):
        try:
            current_img = image
            next_img = self.images[image_number + 1]
            if current_img.amount_of_shows < next_img.amount_of_shows:
                self.images.insert(image_number + 1, self.images.pop(image_number))
                self.__sort_images(current_img, image_number + 1)
        except:
            return

    def __get_by_views(self, relevant_images: dict) -> dict:
        if len(relevant_images.keys()) == 1:
            return relevant_images

        resault_image = {}
        for image in relevant_images.keys():
            if not image is self.last_shown:
                number_in_list = relevant_images[image]
                resault_image[image] = number_in_list
                return resault_image

    def __attr_update(self, image_data: dict):
        for image, image_number in image_data.items():
            image.amount_of_shows -= 1
            if image.amount_of_shows == 0:
                self.images.pop(image_number)
            else:
                self.__sort_images(image, image_number)

            self.last_shown = image
            return image

    def get_image(self, required_categories: set):
        self.__check_extreme()

        valid_categories = self.avaliable_categories & required_categories
        if not valid_categories:
            return None

        relevant_images = self.__check_matching_request(valid_categories)
        if not relevant_images:
            return None

        resault_image = self.__get_by_views(relevant_images)
        image = self.__attr_update(resault_image)

        return image

    def get_random_image(self):
        self.__check_extreme()

        resault_image = {}
        for number in range(len(self.images)):
            image = self.images[number]

            if not image is self.last_shown:
                resault_image[image] = number
                image = self.__attr_update(resault_image)

                return image


images, categories = create_list(config.data.endpoint)
image_client = ImagesClient(images, categories)
