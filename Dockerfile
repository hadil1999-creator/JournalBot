# Utiliser une image Python officielle
FROM python:3.11

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application tourne (modifie si nécessaire)
EXPOSE 5000  

# Définir la commande pour lancer l'application (modifie si nécessaire)
CMD ["python", "webapp/run.py"]  
