from os import getenv 
from dotenv import load_dotenv
from requests import get
import urllib.parse

def nutritional_info(food):
	"""Return a JSON object with the nutritional info of the given food.
	Relies on the Edamam API, with API keys in .env."""
	load_dotenv() # load app id, key
	url = "https://api.edamam.com/api/nutrition-data"
	payload = {
		"app_id": getenv("NUTR_DETAILS_APP_ID"),
		"app_key": getenv("NUTR_DETAILS_APP_KEY"),
		"ingr": food 
	}

	params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
	response = get(url, params=params)
	return response.json()

def product_from_upc(upc):
	"""Based on the barcode (Universal Product Code), determine what produce it is."""
	load_dotenv() # load app id, key
	url = "https://api.edamam.com/api/food-database/parser"
	payload = {
		"upc": upc,
		"app_id": getenv("FOOD_DATA_APP_ID"),
		"app_key": getenv("FOOD_DATA_APP_KEY"),
	}
	params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
	response = get(url, params=params)
	return response.json()
