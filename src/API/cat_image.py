import requests
import logging
from utils import config

global_settings = config.get_settings()

MAX_RETRIES = 10
MIN_CAT_IMAGE_WIDTH = 320
MAX_CAT_IMAGE_WIDTH = 1440


def get_url() -> str:
    """Requests a cat image from the cat image API and returns the cat image url"""
    cat_image_extension = ""
    cat_image_width = 0
    request_attempts = 0

    while (
        cat_image_extension not in [".jpg", "jpeg"]
        or cat_image_width <= MIN_CAT_IMAGE_WIDTH
        or cat_image_width >= MAX_CAT_IMAGE_WIDTH
    ):
        try:
            response = requests.get(
                f"{global_settings.cat_image_api_url}?api_key={global_settings.cat_image_api_key}"
            )
            response.raise_for_status()
            response_json = response.json()
        except Exception as e:
            logging.debug(e)
            continue

        cat_image = response_json[0]
        cat_image_url = cat_image.get("url")

        if cat_image_url is not None:
            cat_image_extension = cat_image_url[-4:] or ""
            cat_image_width = cat_image.get("width") or 0

        if request_attempts == MAX_RETRIES:
            logging.error("unable to retrieve suitable cat image")
            exit()

        request_attempts += 1

    if cat_image_url is None:
        logging.error("api responded without a URL")
        exit()

    return cat_image_url
