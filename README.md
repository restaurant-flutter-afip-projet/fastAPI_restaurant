# fastAPI-restaurant
API en fastAPI pour un mini-projet de réservation pour un resto fictif.

## 1. Requirements :

    pip install "fastapi[standard]"
	pip install uvicorn
    pip install pymysql
    pip install sqlalchemy
    pip install pydantic_settings
    pip install pydantic

## 2. Installer la base de données :

Pour installer la base de données, commencer par créer une nouvelle base de données, si vous l'avez déja fait, passez cette étape.

Ensuite, rendez-vous dans le fichier "backend/core/config.py".
Copiez-y le contenu suivant :

    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
		DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/db_name"

		class Config:
			env_file = ".env"
		


Remplacez les élements suivants :
- user : Le nom d'utilisateur pour accéder à la BDD
- password : Le mot de passe pour accéder à la BDD
- db_name : Le nom de votre base de donnée

Puis créez un fichier ".env" au même endroit que "config.py".
Ouvrez-le et ajoutez-y le contenu suivant :

    DATABASE_URL="mysql+pymysql://user:password@localhost:3306/db_name"
	
Remplacez encore une fois les élements suivants :
- user : Le nom d'utilisateur pour accéder à la BDD
- password : Le mot de passe pour accéder à la BDD
- db_name : Le nom de votre base de donnée


Enfin, executez le fichier "backend/db/init_db.py" pour créer les tables : 

    python -m backend.db.init_db

Une fois ces étapes effectuées, la base de données devrait être prête à l'utilisation.