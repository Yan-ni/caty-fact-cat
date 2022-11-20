#!/usr/bin/python3
import requests
import json
from dotenv import load_dotenv
import os
from io import BytesIO
from PIL import Image

load_dotenv()

def get_fact() -> str:
	"""Requests cat fact api

	Returns:
		str: the fact with "Did you know ! " at the beginning
	"""
	api_url_cat_fact = f'https://meowfacts.herokuapp.com/'
	
	response = requests.get(api_url_cat_fact)

	cat_fact = response.json()["data"][0]

	return f'Did you know ! {cat_fact}'

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
		print(image_width)
	
	return cat_image_url

get_image()


if __name__ == '__main__':
	exit()
	ig_user_id = os.getenv('IG_USER_ID')

	print('getting cat image...')
	try:
		image_url = get_image()
	except e:
		print('failed.')
		print(e)
		exit()

	print('getting cat fact...')
	try:
		caption = get_fact()
	except e:
		print('failed.')
		print(e)
		exit()

	access_token = os.getenv('ACCESS_TOKEN')

	print('posting image to instagram...')
	res = requests.post(f'https://graph.facebook.com/v15.0/{ig_user_id}/media?image_url={image_url}&caption={caption}&access_token={access_token}')
	res = res.json()

	if res.get('id') is None:
		print('failed.')
		print(json.dumps(res, indent=2))
		exit()

	container = res['id']
	print('publishing the image...')
	res = requests.post(f'https://graph.facebook.com/v15.0/{ig_user_id}/media_publish?creation_id={container}&access_token={access_token}')
	res = res.json()

	if res.get('id') is None:
		print('failed.')
		print(json.dumps(res, indent=2))
		exit()

	print('image published successfully.')