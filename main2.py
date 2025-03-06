import tweepy
import TokenAPI
import CompteASuivre  

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        
        print(f"🆕 Nouveau tweet de @{status.user.screen_name}: {status.text}")

    def on_error(self, status_code):
        if status_code == 420:
            # En cas d'erreur de limite de taux, on attend avant de continuer
            print("Erreur 420: Limite de taux atteinte. Attente...")
            return False  # Cela déconnecte le stream


auth = tweepy.OAuth2BearerHandler(TokenAPI.BEARER_TOKEN)
api = tweepy.API(auth)

listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

user_id = api.get_user(screen_name=CompteASuivre.USERNAME).id_str

stream.filter(follow=[user_id])
