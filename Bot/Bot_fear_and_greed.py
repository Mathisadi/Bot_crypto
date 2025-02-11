import json
import pandas as pd

# Spécifiez le chemin vers votre fichier JSON
path = "./Data/fear-and-greed.json"

# Ouvrir et lire le fichier JSON
with open(path, "r", encoding="utf-8") as f:
    contenu = json.load(f)

# Créer un DataFrame à partir de la liste de dictionnaires associée à la clé "data"
df = pd.DataFrame(contenu["data"])

# 3 scope