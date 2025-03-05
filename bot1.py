import time
import requests
import TokenAPI

def get_tweet_text(tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}
    
    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()["data"]["text"]
        
        elif response.status_code == 429:  # Trop de requêtes
            reset_time = int(response.headers.get("x-rate-limit-reset", time.time() + 60))
            wait_time = reset_time - int(time.time())
            print(f"Trop de requêtes. Pause de {wait_time} secondes...")
            time.sleep(wait_time)
        
        else:
            print(f"Erreur {response.status_code}: {response.json()}")
            return None

if __name__ == "__main__":
    tweet_id = input("Entrez l'ID du tweet : ")
    tweet_text = get_tweet_text(tweet_id)

    if tweet_text:
        print("\nTexte du tweet:", tweet_text)
