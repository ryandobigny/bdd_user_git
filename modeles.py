from extensions import db

#

#########################################
### Créer les colonnes de la tables ####
########################################


class User(db.Model):
    __tablename__ = 'users'
    # Clé primaire, id de chaque user
    id = db.Column(db.Integer, primary_key=True)
    # nom_user de 64 caractères au max, unique (sans doublons) 
    # Créer un index sur la colonne pour optimiser les performances 
    # lors de la recherche et du filtrage des données basées sur cette colonne. 
    nom_user = db.Column(db.String(64), unique=True, index=True)
    #Mot de passe de 128 caractères au maximum
    mdp = db.Column(db.String(128))
    
    # Relation many-to-many avec Groupe
    groupes = db.relationship('Groupe', secondary='user_groupes', backref='users', 
                             lazy='dynamic')

    '''
    lazy='dynamic' : Cette option pour la relation signifie que les éléments associés
    (dans ce cas, les groupes) ne sont pas chargés immédiatement. 
    À la place, SQLAlchemy retourne un objet de requête (Query object) 
    que tu peux utiliser pour exécuter des requêtes supplémentaires, 
    comme filtrer, trier, etc.
    on peut mettre lazy='select' SQLAlchemy chargera les groupes associés 
    dès que tu accèdes à user.groupes, ce qui simplifie le code si tu n'as pas besoin 
    d'effectuer des requêtes dynamiques supplémentaires.
    '''
    
    def __repr__(self):
        # renvoie une chaine de représentation d'un user
        return f"User:  {self.nom_user}"


class Groupe(db.Model):
    __tablename__ = 'groupes'
    id_gr = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<Groupe {self.nom}>'

# Table d'association pour la relation many-to-many entre User et Group
user_groupes = db.Table('user_groupes',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('id_groupe', db.Integer, db.ForeignKey('groupes.id_gr'), primary_key=True)
)
