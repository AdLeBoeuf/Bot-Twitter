import tweepy
import TokenAPI  # Fichier contenant BEARER_TOKEN
import CompteASuivre  # Fichier contenant le compte à suivre

# 1. Authentification avec Tweepy pour récupérer des informations sur l'utilisateur
client = tweepy.Client(bearer_token=TokenAPI.BEARER_TOKEN)

# 2. Récupérer l'ID utilisateur avec le username
user = client.get_user(username=CompteASuivre.USERNAME)
user_id = user.data.id

# 3. Créer un flux en temps réel pour écouter les tweets
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # Cette méthode sera appelée chaque fois qu'un tweet du compte suivi est posté
        print(f"🆕 Nouveau tweet de @{tweet.author_id}: {tweet.text}")

# 4. Démarrer le stream pour surveiller les tweets du compte spécifié
stream_client = MyStream(bearer_token=TokenAPI.BEARER_TOKEN)

# 5. Ajouter une règle pour surveiller les tweets du compte
stream_client.add_rules(tweepy.StreamRule(f"from:{user_id}"))

# 6. Démarrer l'écoute du flux en temps réel
stream_client.filter()
