from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle  # Pour importer/exporter les cookies
from CompteASuivre import USERNAME

# Configuration de Selenium pour ne pas afficher de fenêtre
options = Options()
options.headless = True  # Lancer le navigateur en mode headless (sans interface)
driver = webdriver.Chrome(options=options)

url = f"https://twitter.com/{USERNAME}"
dernier_tweet = None

# 1. Donne 15 secondes pour la connexion initiale
driver.get(url)
time.sleep(15)  # Le temps de te connecter

# 2. Enregistre les cookies après la connexion (une fois connecté manuellement)
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)

print("Cookies enregistrés, tu peux maintenant redémarrer le script.")

# Ferme le navigateur après avoir enregistré les cookies
driver.quit()

# 3. Redémarrer le script avec un délai court et réutiliser les cookies
driver = webdriver.Chrome(options=options)
driver.get("https://twitter.com")

# Charger les cookies à partir du fichier
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Rafraîchir la page pour appliquer les cookies
driver.refresh()
time.sleep(3)  # Attends que la page se charge complètement

# Lancer la surveillance des tweets avec un délai de 1 seconde
while True:
    try:
        driver.get(url)  # Récupère la page de l'utilisateur
        time.sleep(3)  # Attends que la page se charge

        # Trouver les tweets
        tweets = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweetText']")
        
        # Si des tweets sont trouvés
        if tweets:
            tweet_text = tweets[0].text.strip()  # Récupérer et nettoyer le texte du tweet
            if tweet_text != dernier_tweet:  # Vérifier si c'est un nouveau tweet
                print(f"Nouveau tweet détecté : {tweet_text}")
                dernier_tweet = tweet_text  # Mettre à jour le dernier tweet
            else:
                print("Aucun nouveau tweet.")
        else:
            print("Aucun tweet trouvé.")

        # Vérifier toutes les 1 seconde pour voir si un nouveau tweet est posté
        time.sleep(1)

    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)  # Pause plus longue en cas d'erreur
