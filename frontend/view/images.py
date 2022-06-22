from flask import Blueprint, render_template, request

from frontend.client.images import ImagesClient


image_repo = ImagesClient()
view = Blueprint('images', __name__)


@view.route('/', methods=['GET'])
def show_image():
    categories = request.args.getlist('category[]', type=str)

    if categories and categories != ['']:
        image = image_repo.get_image(set(categories))
        if not image:
            return render_template(
                'image.html',
                message='There are not images which match to requested categories: {}'.format(
                    ', '.join(categories)
                ),
            )
    else:
        image = image_repo.get_random_image()

    return render_template(
        'image.html',
        image_path=image.url,
        categories=image.categories,
    )
