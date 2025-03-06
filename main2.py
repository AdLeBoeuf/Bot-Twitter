import tweepy
import TokenAPI  # Fichier contenant BEARER_TOKEN
import CompteASuivre  # Fichier contenant le compte à suivre

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # Cette méthode sera appelée chaque fois qu'un tweet du compte suivi est posté
        print(f"🆕 Nouveau tweet de @{tweet.author_id}: {tweet.text}")

# Authentification avec Tweepy
client = MyStream(bearer_token=TokenAPI.BEARER_TOKEN)

# Démarrer le stream pour surveiller les tweets du compte spécifié
# Ici, on récupère l'ID de l'utilisateur pour le compte que tu veux suivre
user = client.get_user(username=CompteASuivre.USERNAME)
user_id = user.data.id

# Démarrer l'écoute du flux en temps réel pour ce compte
client.add_rules(tweepy.StreamRule(f"from:{user_id}"))
client.filter()
