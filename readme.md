# Projet de Récupération de Tweets en Temps Réel

Ce projet a pour objectif de récupérer les textes des tweets d'un ou plusieurs comptes Twitter spécifiques dès leur publication, en utilisant l'API X. Le script est conçu pour s'exécuter en continu sans nécessiter de redémarrage manuel, et il gère les limitations de l'API.

## Fonctionnalités

- **Extraction du texte des tweets** : Récupère le texte d'un tweet dès qu'il est posté.
- **Gestion du cooldown de l'API** : Le script attend automatiquement le temps nécessaire lorsque la limite de requêtes de l'API est atteinte.
- **Récupération en temps réel** : Utilisation du streaming de l'API X pour capter les nouveaux tweets dès leur publication.
- **Stockage des données** : Permet de stocker les tweets extraits dans un fichier (ou base de données selon les besoins).

## Prérequis

- Python 3.x
- Bibliothèque `tweepy` pour interagir avec l'API X
- Clés API de l'API X pour l'authentification

## Étapes du Projet

### Étape 1 : Extraction du texte d'un tweet
- **Objectif** : Récupérer le texte d'un tweet lorsqu'il est posté.
- **Méthode** : Utiliser l'API X pour accéder aux tweets d'un compte spécifique.

### Étape 2 : Gérer le cooldown de l'API
- **Objectif** : Gérer la limite de requêtes imposée par l'API X afin d'éviter de devoir relancer manuellement le script lorsque cette limite est atteinte.
- **Méthode** : Implémenter une logique qui attend automatiquement la fin du cooldown avant de reprendre l'extraction.

### Étape 3 : Récupérer des tweets en temps réel (Streaming)
- **Objectif** : Utiliser le streaming de l'API X pour écouter les tweets en temps réel et récupérer ceux publiés sans redémarrer le script manuellement.
- **Méthode** : Configurer l'écoute des tweets en temps réel via l'API de streaming de X.

### Étape 4 : Gérer les erreurs et exceptions
- **Objectif** : Assurer que le script ne plante pas en cas d'erreurs (p. ex. connexion perdue, erreur API).
- **Méthode** : Implémenter une gestion d'erreurs qui redémarre le processus en cas de problème.

### Étape 5 : Stocker les tweets récupérés
- **Objectif** : Enregistrer les tweets récupérés pour pouvoir les analyser ou les utiliser plus tard.
- **Méthode** : Sauvegarder les tweets extraits dans un fichier ou une base de données.

### Étape 6 : Traitement des données
- **Objectif** : Ajouter un traitement des tweets récupérés pour extraire des informations supplémentaires (p. ex. analyse de sentiment, extraction de hashtags).
- **Méthode** : Traiter les tweets extraits selon les besoins du projet.


