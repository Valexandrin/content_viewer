from frontend.data.db import db


class ImagesClient:

    def get_image(self):
        category = db.config['flight']
        return category[0]
