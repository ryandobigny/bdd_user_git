from flask import redirect, url_for
from modeles import User, Groupe, db

def enregistrer_routes (app): 
    @app.route("/")
    def index():
        ch = "<h1>Liste des users: </h1><ol>"
        users = User.query.all()
        for user in users:
            ch += "<li>"+user.nom_user+"</li>"
        ch += "</ol><h1>Liste des groupes: </h1><ol>"         
        groupes = Groupe.query.all()
        users = User.query.all()
        for gr in groupes:
            ch += "<li>"+gr.nom+"</li>"
        ch += "</ol>"
        return ch

    @app.route('/add_user/<nom>/<mdp>')
    def add_user(nom, mdp):
        db.session.add(User(nom_user=nom, mdp=mdp))
        db.session.commit()
        return redirect(url_for("index"))     

    @app.route('/add_gr/<nom>')
    def add_groupe(nom):
        db.session.add(Groupe(nom=nom))
        db.session.commit()
        return redirect(url_for("index"))    

    @app.route('/attacher_groupes/<nom_u>/<noms_gr>')
    def attacher_user_aux_groupes(nom_u, noms_gr):
        # Récupérer l'utilisateur par son nom
        user = User.query.filter_by(nom_user=nom_u).first()
        if not user:
            return f"Utilisateur avec le nom {nom_u} introuvable.", 404

        # Convertir group_ids en une liste de noms
        lst_noms_gr = [gnom for gnom in noms_gr.split(",")]

        # Récupérer les groupes correspondants
        groupes = Groupe.query.filter(Groupe.nom.in_(lst_noms_gr)).all()
        if not groupes:
            return f"Groupes avec les noms {noms_gr} introuvables.", 404

        # Ajouter chaque groupe à l'utilisateur
        for group in groupes:
            user.groupes.append(group)

        db.session.commit()

        return f"Les groupes {noms_gr} ont été attachés à l'utilisateur '{user}'."

    