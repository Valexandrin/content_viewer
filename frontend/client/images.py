from frontend.data.img_list import images_list, total_shows


class ImagesClient:
    def __init__(self) -> None:
        self.images_shown = 0
        self.avaliable_shows = total_shows
        self.images = images_list

    def get_image(self, categories):
        self.images_shown += 1
        relevant_images = {}
        required_categories = set(categories)

        for image in self.images:
            overlap = len(required_categories & image.categories)
            if overlap:
                relevant_images[image] = overlap

        relevant_images = dict(sorted(relevant_images.items(), key=lambda item: item[1], reverse=True))

        resault_image = self.sort_by_shows(relevant_images)
        resault_image.amount_of_shows -= 1

        return resault_image

    def sort_by_shows(self, relevant_images):
        for image in relevant_images.keys():
            if image.amount_of_shows < self.avaliable_shows:
                print(self.avaliable_shows)
                return image
            return image

    def get_random_image(self):
        return images_list[1]
