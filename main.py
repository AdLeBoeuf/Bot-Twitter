import time
import requests
import TokenAPI
import CompteASuivre

def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("id")
    else:
        print(f"Erreur {response.status_code}: {response.json()}")
        return None

def get_latest_tweets(user_id, last_seen_id=None):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}
    params = {
        "tweet.fields": "created_at",
        "max_results": 5
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tweets = response.json().get("data", [])
        new_tweets = [tweet for tweet in tweets if last_seen_id is None or tweet["id"] > last_seen_id]
        return new_tweets
    else:
        print(f"Erreur {response.status_code}: {response.json()}")
        return []

if __name__ == "__main__":
    username = CompteASuivre.USERNAME
    user_id = get_user_id(username)

    if user_id:
        last_seen_id = None
        print(f"Surveillance des tweets de @{username}...")

        while True:
            tweets = get_latest_tweets(user_id, last_seen_id)
            
            if tweets:
                for tweet in reversed(tweets):
                    print(f"\n🆕 Nouveau tweet ({tweet['created_at']}) : {tweet['text']}")
                    last_seen_id = tweet["id"]  
            
            time.sleep(900)  # Vérification toutes les 15 secondes
