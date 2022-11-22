#!/usr/bin/python3
import requests
import json
from dotenv import load_dotenv
import os
from io import BytesIO
from PIL import Image
from urllib import parse

load_dotenv()

hashtags = ['cat', 'cats', 'catsofinstagram', 'cats_of_instagram', 'catlove', 'catlover', 'catlovers', 'catloversclub', 'catlife', 'cats_of_world', 'catphoto', 'instacat', 'catoftheday', 'cats_of_day', 'catstagram', 'catsagram']

def get_fact() -> str:
	"""Requests cat fact api

	Returns:
		str: the fact with "Did you know ! " at the beginning
	"""
	api_url_cat_fact = f'https://meowfacts.herokuapp.com/'
	
	response = requests.get(api_url_cat_fact)

	cat_fact = response.json()["data"][0]

	return f'Did you know ! {cat_fact}'

def get_caption() -> str:
	fact = get_fact()

	return f'{fact}\r\n\r\n{" ".join([f"#{hashtag}" for hashtag in hashtags])}'

def get_image() -> str:
	"""Requests cat iamge api until getting a valid image to post

	Returns:
		str: the img url
	"""
	api_key = os.getenv('API_KEY')
	image_extension = ''
	image_width = 0

	while image_extension not in ['.jpg', 'jpeg'] or image_width <= 320 or image_width >= 1440:
		response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={api_key}')
		cat_image_url = response.json()[0]["url"]
		image_extension = cat_image_url[-4:]

		response = requests.get(cat_image_url)
		img = Image.open(BytesIO(response.content))

		image_width, _ = img.size
	
	return cat_image_url

if __name__ == '__main__':
	ig_user_id = os.getenv('IG_USER_ID')

	try:
		print('getting cat image...')
		image_url = get_image()
		print('getting cat fact...')
		caption = get_caption()
	except e:
		print('failed.')
		print(e)
		exit()

	access_token = os.getenv('ACCESS_TOKEN')

	print('creating instagram media...')
	image_url = parse.quote(image_url, safe='')
	caption = parse.quote(caption, safe='')
	res = requests.post(f'https://graph.facebook.com/v15.0/{ig_user_id}/media?image_url={image_url}&caption={caption}&access_token={access_token}')
	res = res.json()

	if 'id' not in res:
		print('failed.')
		print(json.dumps(res, indent=2))
		exit()

	media_id = res['id']
	print('publishing the media...')
	res = requests.post(f'https://graph.facebook.com/v15.0/{ig_user_id}/media_publish?creation_id={media_id}&access_token={access_token}')
	res = res.json()

	if 'id' not in res:
		print('failed.')
		print(json.dumps(res, indent=2))
		exit()

	print('media published successfully.')