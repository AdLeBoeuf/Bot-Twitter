import time
import requests
import TokenAPI  # Fichier contenant BEARER_TOKEN
import CompteASuivre  # Fichier contenant le compte à suivre

# Obtenir l'ID de l'utilisateur depuis son @pseudo
def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("id")
    else:
        print(f"Erreur {response.status_code}: {response.json()}")
        return None

# Récupérer les 5 derniers tweets mais ne garder que le plus récent
def get_latest_tweet(user_id):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}
    params = {
        "tweet.fields": "created_at,referenced_tweets",
        "max_results": 5  # Récupérer jusqu'à 5 derniers tweets
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tweets = response.json().get("data", [])

        # Filtrer pour ne garder que les tweets originaux (pas de retweets)
        tweets = [
            tweet for tweet in tweets
            if "referenced_tweets" not in tweet or tweet["referenced_tweets"][0]["type"] != "retweeted"
        ]

        return tweets[0] if tweets else None  # Retourner uniquement le plus récent tweet
    else:
        print(f"Erreur {response.status_code}: {response.json()}")
        return None

if __name__ == "__main__":
    username = CompteASuivre.USERNAME  # Récupération automatique du pseudo
    user_id = get_user_id(username)

    if user_id:
        print(f"🔍 Surveillance des tweets de @{username}...")

        last_tweet_id = None  # On stocke l'ID du dernier tweet affiché

        while True:
            tweet = get_latest_tweet(user_id)

            if tweet and tweet["id"] != last_tweet_id:  # Si un nouveau tweet est détecté
                print(f"\n🆕 Nouveau tweet ({tweet['created_at']}) : {tweet['text']}")
                last_tweet_id = tweet["id"]  # Mise à jour du dernier tweet connu

            time.sleep(60)  # Vérification toutes les 60 secondes
