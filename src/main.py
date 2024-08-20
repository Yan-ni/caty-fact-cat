import API
import utils

def main():
	utils.setup_logging()
	logging.info('getting cat image')
	cat_image_url = API.CatImage.get_url()

	logging.info('getting cat fact')
	cat_fact = API.CatFact.get_fact()

	ig_caption = API.Instagram.get_caption(cat_fact)

	logging.info('creating instagram media')
	ig_media_id = API.Instagram.create_media(cat_image_url, ig_caption)

	logging.info('publishing the media')
	ig_media_publish_id = API.Instagram.publish_media(ig_media_id)

	logging.info('media published successfully')

# Main function
if __name__ == '__main__':
	main()
