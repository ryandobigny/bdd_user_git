from app import creer_app, db  # Importer la fonction factory et db
from modeles import User, Groupe  # Importer les modèles

# Créer l'application
app = creer_app()

if __name__ == "__main__":
    # Exemple d'initialisation de la base de données
    with app.app_context():
        print("Initialisation de la base de données...")
        db.drop_all()  # Supprimer toutes les tables
        db.create_all()  # Créer toutes les tables
        print("Base de données initialisée.")

        # Ajouter des exemples de données
        user1 = User(nom_user="John", mdp="admin123")
        user2 = User(nom_user="Susan", mdp="secret")
        group1 = Groupe(nom="VCOD")
        group2 = Groupe(nom="Promo_SD3")

        db.session.add_all([user1, user2, group1, group2])
        db.session.commit()

    # Lancer l'application Flask
    app.run(debug=True, port=5000)
