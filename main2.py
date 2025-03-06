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
        response = requests.get(url, headers=headers, timeout=10)  # Ajout du timeout pour éviter que le script ne reste bloqué
        
        if response.status_code != 200:
            print(f"Erreur HTTP: {response.status_code}")
            time.sleep(60)  # Attendre avant de réessayer
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")

        # Affiche la structure HTML pour vérifier le contenu
        print(soup.prettify())  # À commenter une fois que tu as inspecté la structure

        # Trouver le dernier tweet avec un sélecteur CSS plus robuste
        tweet = soup.find("div", {"data-testid": "tweetText"})
        if tweet:
            tweet_text = tweet.text.strip()  # Récupérer et nettoyer le texte du tweet
            if tweet_text != dernier_tweet:
                print(f"Nouveau tweet détecté : {tweet_text}")
                dernier_tweet = tweet_text
            else:
                print("Aucun nouveau tweet.")
        else:
            print("Aucun tweet trouvé.")
        
        # Vérifier toutes les 30 secondes pour réduire la charge sur le serveur
        time.sleep(30)

    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)  # Pause plus longue en cas d'erreur
