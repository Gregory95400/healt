Health Calculator Microservice
Ce projet est un microservice Flask qui calcule les métriques de santé telles que l'IMC (Indice de Masse Corporelle) et le TMB (Taux Métabolique Basal) via une API REST.

Prérequis
Python 3.10 ou supérieur
pip (gestionnaire de paquets Python)
Docker (optionnel, pour la conteneurisation)
Installation
Cloner le dépôt :


git clone <URL_DU_DEPOT>
cd healt
Créer un environnement virtuel :

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.


python3 -m venv venv
source venv/bin/activate
Installer les dépendances :

Utilisez pip pour installer les dépendances nécessaires à partir du fichier requirements.txt.


pip install -r requirements.txt
Exécution de l'Application
Pour lancer l'application Flask en local, exécutez la commande suivante :


python app.py
L'application sera accessible à l'adresse http://127.0.0.1:5000.
