import requests
from bs4 import BeautifulSoup
import time
from CompteASuivre import USERNAME

# Remplace "username" par le compte X à tracker

url = f"https://twitter.com/{USERNAME}"
dernier_tweet = None

while True:
    try:
        # Récupérer la page X
        headers = {"User-Agent": "Mozilla/5.0"}  # Simule un navigateur
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Trouver le dernier tweet (balise approximative, peut nécessiter ajustement)
        tweet = soup.find("div", {"data-testid": "tweetText"})
        if tweet and tweet.text != dernier_tweet:
            print(f"Nouveau tweet détecté : {tweet.text}")
            dernier_tweet = tweet.text
        else:
            print("Aucun nouveau tweet.")

        # Vérifier toutes les 5 secondes (ajustable)
        time.sleep(5)

    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)  # Pause plus longue en cas d’erreur