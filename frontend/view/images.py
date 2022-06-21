from flask import Blueprint, render_template, request

from frontend.client.images import ImagesClient

image_repo = ImagesClient()
view = Blueprint('images', __name__)


@view.route('/', methods=['GET'])
def show_image():
    category = request.args.getlist('category[]', type=str)

    if category and category != ['']:
        image = image_repo.get_image()
        return render_template(
            'image.html',
            image_path=image.url,
        )

    image = image_repo.get_random_image()
    return render_template(
        'image.html',
        image_path=image.url,
    )
