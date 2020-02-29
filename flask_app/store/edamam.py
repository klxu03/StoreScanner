from os import getenv 
from dotenv import load_dotenv
from requests import get
import urllib.parse

load_dotenv() # load app id, key
print(getenv("APP_ID"))
print(getenv("APP_KEY"))
url = "https://api.edamam.com/api/nutrition-data"
payload = {
	"app_id": getenv("APP_ID"),
	"app_key": getenv("APP_KEY"),
	"ingr": "1 large apple" 
}
params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
response = get(url, params=params)
print(response.json)