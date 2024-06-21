import API

def main():
	print('[PROCESS] getting cat image...')
	cat_image_url = API.CatImage.get_url()

	if cat_image_url is None:
		print('[EXIT] failed getting cat image.')
		exit()

	print('[PROCESS] getting cat fact...')
	cat_fact = API.CatFact.get_fact()

	if cat_fact is not None:
		ig_caption = API.Instagram.get_caption(cat_fact)

	print('[PROCESS] creating instagram media...')
	ig_media_id = API.Instagram.create_media(cat_image_url, ig_caption)

	if ig_media_id is None:
		print('[EXIT] failed creating instagram media.')
		exit()

	print('[PROCESS] publishing the media...')
	ig_media_publish_id = API.Instagram.publish_media(ig_media_id)

	if ig_media_publish_id is None:
		print('[EXIT] failed publishing instagram media.')
	else:
		print('[PROCESS] media published successfully.')

# Main function
if __name__ == '__main__':
	main()
