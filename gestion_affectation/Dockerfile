# Utilisez une image de base compatible avec Django
FROM python:3.9
# Définissez le répertoire de travail dans le conteneur
WORKDIR /app
# Copiez les fichiers requirements.txt dans le conteneur
COPY requirements.txt .
# Installez les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt
# Copiez le reste du code source dans le conteneur
COPY . .
# Exposez le port utilisé par l'application (par défaut, c'est 8000 pour Django)
EXPOSE 8000
# Définissez les variables d'environnement pour Django
ENV DJANGO_SETTINGS_MODULE=gestion_affectation.settings.production
# Exécutez les migrations et lancez le serveur Django lors du démarrage du conteneur
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]