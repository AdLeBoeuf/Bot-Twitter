import requests
import TokenAPI


def get_tweet_text(tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    headers = {"Authorization": f"Bearer {TokenAPI.BEARER_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        tweet_data = response.json()
        return tweet_data["data"]["text"]
    else:
        print("Erreur:", response.status_code, response.json())
        return None

if __name__ == "__main__":
    tweet_id = input("Entrez l'ID du tweet : ")
    tweet_text = get_tweet_text(tweet_id)
    
    if tweet_text:
        print("\nTexte du tweet:", tweet_text)

