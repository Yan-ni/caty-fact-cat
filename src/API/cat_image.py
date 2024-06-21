import requests
from .config import CAT_IMAGE_API_KEY

class CatImage:
  @staticmethod
  def get_url() -> str:
    """Requests a cat iamge from the cat image API and returns the cat image url"""
    cat_image_extension = ''
    cat_image_width = 0

    request_attempts = 0

    while cat_image_extension not in ['.jpg', 'jpeg'] or cat_image_width <= 320 or cat_image_width >= 1440:
      try:
        response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={CAT_IMAGE_API_KEY}')
        response.raise_for_status()
        response_json = response.json()
      except Exception as e:
        print(f'[EXCEPTION] {e}')
        continue

      cat_image = response_json[0]
      cat_image_url = cat_image.get('url')
      
      if cat_image_url is not None:
        cat_image_extension = cat_image_url[-4:] or ''
        cat_image_width = cat_image.get("width") or 0

      if request_attempts == 10:
        return None

      request_attempts += 1

    if cat_image_url is None:
      return None

    return cat_image_url