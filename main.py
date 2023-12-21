#!/usr/bin/python3

# Imports
from dotenv import load_dotenv
import os
from urllib import parse
import requests
import json

# Load environement variables
load_dotenv()

# Global variables
IG_USER_ID = os.getenv('IG_USER_ID')
IG_ACCESS_TOKEN = os.getenv('IG_ACCESS_TOKEN')
IG_API_VERSION = os.getenv('IG_API_VERSION')
CAT_IMAGE_API_KEY = os.getenv('CAT_IMAGE_API_KEY')

# Functions
def get_fact() -> str:
	"""Requests a cat fact from cat fact API and returns the fact concatenated with "Did you know ! " at the start of the fact."""
	api_url_cat_fact = f'https://meowfacts.herokuapp.com/'
	
	response = requests.get(api_url_cat_fact)

	cat_fact = response.json()["data"][0]

	return f'Did you know ! {cat_fact}'

def get_ig_caption() -> str:
	"""Genrate the instagram post caption with the cat fact and hashtags"""
	hashtags = ['cat', 'cats', 'catsofinstagram', 'cats_of_instagram', 'catlove', 'catlover', 'catlovers', 'catloversclub', 'catlife', 'cats_of_world', 'catphoto', 'instacat', 'catoftheday', 'cats_of_day', 'catstagram', 'catsagram']
	fact = get_fact()

	return f'{fact}\r\n\r\n{" ".join([f"#{hashtag}" for hashtag in hashtags])}'

def get_cat_image_url() -> str:
	"""Requests a cat iamge from the cat image API and returns the cat image url"""
	cat_image_extension = ''
	cat_image_width = 0

	while cat_image_extension not in ['.jpg', 'jpeg'] or cat_image_width <= 320 or cat_image_width >= 1440:
		response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={CAT_IMAGE_API_KEY}')
		response = response.json()
		cat_image = response[0]
		cat_image_url = cat_image.get("url") or ""
		cat_image_extension = cat_image_url[-4:]
		cat_image_width = cat_image.get("width") or 0

	return cat_image_url

def create_ig_media(image_url: str, caption= "") -> str:
	"""Creates an Instagram media using Instagram graph API"""
	image_url = parse.quote(image_url, safe='')
	caption = parse.quote(caption, safe='')
	
	res = requests.post(f'https://graph.facebook.com/{IG_API_VERSION}/{IG_USER_ID}/media?image_url={image_url}&caption={caption}&access_token={IG_ACCESS_TOKEN}')
	res = res.json()

	ig_media_id = res.get('id')

	if not ig_media_id:
		raise Exception(json.dumps(res, indent=2))

	return ig_media_id

def publish_ig_media(media_id: str) -> None:
	"""Publishes an Instagram media using Instagram graph API"""
	res = requests.post(f'https://graph.facebook.com/{IG_API_VERSION}/{IG_USER_ID}/media_publish?creation_id={media_id}&access_token={IG_ACCESS_TOKEN}')
	res = res.json()

	if 'id' not in res:
		raise Exception(json.dumps(res, indent=2))

# Main function
if __name__ == '__main__':
	try:
		print('getting cat image...')
		cat_image_url = get_cat_image_url()

		print('getting cat fact...')
		caption = get_ig_caption()

		print('creating instagram media...')
		ig_media_id = create_ig_media(cat_image_url, caption)

		print('publishing the media...')
		publish_ig_media(ig_media_id)

		print('media published successfully.')
	except Exception as e:
		print('failed.')
		print(e)
