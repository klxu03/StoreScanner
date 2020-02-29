from os import getenv 
from dotenv import load_dotenv
from requests import get
import urllib.parse

load_dotenv() # load app id, key

def nutritional_info(food):
	"""Return a JSON object with the nutritional info of the given food.
	Relies on the Edamam API, with API keys in .env."""
	url = "https://api.edamam.com/api/nutrition-data"
	payload = {
		"app_id": getenv("APP_ID"),
		"app_key": getenv("APP_KEY"),
		"ingr": food 
	}

	params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
	response = get(url, params=params)
	return response.json()