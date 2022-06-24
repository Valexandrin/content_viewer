from flask import Blueprint, render_template, request

from frontend.client.images import image_client

view = Blueprint('images', __name__)


@view.route('/', methods=['GET'])
def show_image():
    categories = request.args.getlist('category[]', type=str)

    if categories and categories != ['']:
        image = image_client.get_image(set(categories))
    else:
        image = image_client.get_random_image()

    if not image:
        return render_template(
            'image.html',
            message='Not found images matching categories: {categories}'.format(
                categories=', '.join(categories),
            ),
        )

    return render_template(
        'image.html',
        image_path=image.url,
        image_name=image.name,
    )
