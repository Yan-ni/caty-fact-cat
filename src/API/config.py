from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

IG_USER_ID = os.getenv("IG_USER_ID")
IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
IG_API_VERSION = os.getenv("IG_API_VERSION")
CAT_IMAGE_API_KEY = os.getenv("CAT_IMAGE_API_KEY")
