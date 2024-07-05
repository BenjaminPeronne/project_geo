# <center> Web Services REST avec Django </center>

Prénom : <em>Aymerick</em>

Nom : <em>LAURETTA-PERONNE</em>

----

# Project Geo

## Description

Project Geo est une application web permettant de visualiser la géolocalisation des étudiants et des universités sur une carte interactive OpenStreetMap. Les adresses saisies pour les étudiants et les universités sont automatiquement converties en coordonnées géographiques grâce au service de géocodage de Nominatim.

## Prérequis

- Python 
- Django 
- Geopy
- Leaflet 

## Installation

1. Clonez le dépôt du projet :

    ```bash
    git clone https://github.com/votre-nom-utilisateur/project_geo.git
    cd project_geo
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations pour créer les tables de la base de données :

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Créez un superutilisateur pour accéder à l'admin de Django :

    ```bash
    python manage.py createsuperuser
    ```

6. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

## Utilisation

1. Accédez à l'interface d'administration de Django pour ajouter des universités et des étudiants :
    ```
    http://127.0.0.1:8000/admin
    ```

2. Ajoutez des universités avec leurs adresses, villes, codes postaux et pays.

3. Ajoutez des étudiants avec leurs prénoms, noms, adresses, villes, codes postaux, pays et associez-les à une université.

4. Accédez à la carte interactive pour voir les étudiants géolocalisés :
    ```
    http://127.0.0.1:8000/geo/map/
    ```

## Structure du Projet

- **geolocation** : Application Django contenant les modèles, vues, serializers et templates.
  - **models.py** : Définition des modèles `Universite` et `Etudiant`.
  - **serializers.py** : Définition des serializers pour les modèles.
  - **views.py** : Définition des vues pour les API et la carte.
  - **urls.py** : Définition des routes pour l'application.
  - **templates/geolocation/map.html** : Template HTML pour afficher la carte et la liste des étudiants.

## Modèles

### Universite

- `nom` : CharField (max_length=200)
- `adresse` : CharField (max_length=255)
- `ville` : CharField (max_length=100)
- `code_postal` : CharField (max_length=20)
- `pays` : CharField (max_length=100)
- `latitude` : FloatField (null=True, blank=True)
- `longitude` : FloatField (null=True, blank=True)

### Etudiant

- `prenom` : CharField (max_length=100)
- `nom` : CharField (max_length=100)
- `adresse` : CharField (max_length=255)
- `ville` : CharField (max_length=100)
- `code_postal` : CharField (max_length=20)
- `pays` : CharField (max_length=100)
- `universite` : ForeignKey (Universite, on_delete=models.SET_NULL, null=True, blank=True)
- `latitude` : FloatField (null=True, blank=True)
- `longitude` : FloatField (null=True, blank=True)

## API

L'API REST permet de récupérer les informations des étudiants et des universités.

- **Étudiants** : `/geo/etudiants/`
- **Universités** : `/geo/universites/`

