# Created by user at 2024-02-14
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()


#애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    #print(f"__name__:{__name__}")

    #Blueprint등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    
    return app
    
    



