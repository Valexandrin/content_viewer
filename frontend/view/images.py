from flask import Blueprint, render_template

from frontend.client.images import ImagesClient

image_repo = ImagesClient()
view = Blueprint('images', __name__)


@view.route('/')
def show_image():
    image = image_repo.get_image()
    return render_template(
        'image.html',
        image=image.url,
        shows=image.amount_of_shows,
    )
