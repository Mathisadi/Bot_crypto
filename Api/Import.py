from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Keys
API_KEYS = "3e1100bd-16ca-44ae-946d-3ca9461ccb48"

# Fear and greed
url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical'

parameters = {
  'start':'1',
  'limit':'500',
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEYS,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  with open("./Data/fear-and-greed.json", "w", encoding="utf-8") as f:
    # Écrire les données au format JSON dans le fichier
    # ensure_ascii=False permet de garder les caractères spéciaux (si besoin)
    # indent=4 ajoute une indentation pour faciliter la lecture
    json.dump(data, f, ensure_ascii=False, indent=4)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  