from frontend.data.db import db


class ImagesClient:

    def get_image(self):
        images = db['birds']
        img = images[0]

        return img
