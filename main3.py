from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from CompteASuivre import USERNAME

# Configuration du WebDriver
options = Options()
options.headless = True  # Exécute le navigateur en mode sans tête (sans interface graphique)
driver = webdriver.Chrome(options=options)

url = f"https://twitter.com/{USERNAME}"
dernier_tweet = None

while True:
    try:
        driver.get(url)
        time.sleep(3)  # Attendre que la page charge

        # Trouver le dernier tweet
        tweets = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweetText']")
        if tweets:
            tweet_text = tweets[0].text.strip()  # Récupérer le texte du dernier tweet
            if tweet_text != dernier_tweet:
                print(f"Nouveau tweet détecté : {tweet_text}")
                dernier_tweet = tweet_text
            else:
                print("Aucun nouveau tweet.")
        else:
            print("Aucun tweet trouvé.")

        # Vérifier toutes les 30 secondes
        time.sleep(30)

    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)  # Pause plus longue en cas d'erreur
