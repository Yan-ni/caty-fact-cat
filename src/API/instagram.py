from .config import IG_USER_ID, IG_ACCESS_TOKEN, IG_API_VERSION
from urllib import parse
import requests
import json
import logging

class Instagram:
  @staticmethod
  def get_caption(cat_fact:str) -> str:
    """Genrate the instagram post caption with the cat fact and hashtags"""
    hashtags = ['cat', 'cats', 'catsofinstagram', 'cats_of_instagram', 'catlove', 'catlover', 'catlovers', 'catloversclub', 'catlife', 'cats_of_world', 'catphoto', 'instacat', 'catoftheday', 'cats_of_day', 'catstagram', 'catsagram']

    return f'Did you know! {cat_fact}\r\n\r\n{" ".join([f"#{hashtag}" for hashtag in hashtags])}'

  @staticmethod
  def create_media(image_url: str, caption='') -> str:
    """Creates an Instagram media using Instagram graph API"""
    image_url = parse.quote(image_url, safe='')
    caption = parse.quote(caption, safe='')
    
    try:
      response = requests.post(f'https://graph.facebook.com/{IG_API_VERSION}/{IG_USER_ID}/media?image_url={image_url}&caption={caption}&access_token={IG_ACCESS_TOKEN}')
      response.raise_for_status()
    except Exception as e:
      logging.error('error occurred while requesting instagram create media API')
      logging.debug(e)
      exit()

    try:
      response_json = response.json()
    except Exception as e:
      logging.error('error occurred while parsing instagram create media response')
      logging.debug(e)
      logging.debug(response.text)
      exit()

    try:
      ig_media_id = response_json['id']
    except KeyError as e:
      logging.error('error occurred while accessing media id of instagram create media response.')
      logging.debug(e)
      logging.debug(json.dumps(response_json, 4))
      exit()

    return ig_media_id

  @staticmethod
  def publish_media(media_id: str) -> str:
    """Publishes an Instagram media using Instagram graph API"""
    
    try:
      response = requests.post(f'https://graph.facebook.com/{IG_API_VERSION}/{IG_USER_ID}/media_publish?creation_id={media_id}&access_token={IG_ACCESS_TOKEN}')
      response.raise_for_status()
    except Exception as e:
      logging.error('error occurred while requesting instagram publish media API')
      logging.debug(e)
      exit()

    try:
      response_json = response.json()
    except Exception as e:
      logging.error('error occurred while parsing instagram publish media response.')
      logging.debug(e)
      logging.debug(response.text)
      exit()

    try:
      ig_media_publish_id = response_json['id']
    except Exception as e:
      logging.error('error occurred while accessing media id of instagram publish media response.')
      logging.debug(e)
      logging.debug(json.dumps(response_json, 4))
      exit()

    return ig_media_publish_id
