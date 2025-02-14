
# 📄 README - Health Calculator Microservice

Ce fichier README est prêt à être ajouté à votre dépôt Git avec toutes les informations nécessaires.

## 🛑 Prérequis
- **Python** ≥ 3.10
- **pip** (gestionnaire de paquets)
- **Docker** *(optionnel)*

## ⚙️ Installation
### 1️⃣ Cloner le dépôt :
```bash
git clone https://github.com/Gregory95400/healt
cd healt
```
### 2️⃣ Créer et activer l’environnement virtuel :
```bash
python3 -m venv venv
source venv/Scripts/activate
```
### 3️⃣ Installer les dépendances :
```bash
pip install -r requirements.txt
```
## 🚀 Lancer l’Application
```bash
python app.py
```
L’API sera accessible à : **http://127.0.0.1:5000**

## 🐳 Exécuter avec Docker *(optionnel)*
### 1️⃣ Construire l’image :
```bash
docker build -t health-calculator-service .
```
### 2️⃣ Lancer le conteneur :
```bash
docker run -p 5000:5000 health-calculator-service
```


