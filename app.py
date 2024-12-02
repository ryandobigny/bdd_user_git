import os
from flask import Flask
from extensions import db
from routes import enregistrer_routes
import os

def creer_app():
    app = Flask(__name__)
    #basedir = os.path.abspath(os.path.dirname(__file__))
    os.environ.get("DATABASE_URL") = 'postgresql://bdd_user_user:zG60BRbme7UcbaZV6MrEMRgDtw0IqTTs@dpg-ct6mtoqj1k6c73ahneog-a.oregon-postgres.render.com/bdd_user'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    
    #postgresql://bdd_user_user:zG60BRbme7UcbaZV6MrEMRgDtw0IqTTs@dpg-ct6mtoqj1k6c73ahneog-a.oregon-postgres.render.com/bdd_user
    
    # user:   bdd_user_user
    # mdp:    zG60BRbme7UcbaZV6MrEMRgDtw0IqTTs
    # host:   dpg-ct6mtoqj1k6c73ahneog-a.oregon-postgres.render.com
    # dbname: bdd_user

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    enregistrer_routes(app)
    return app