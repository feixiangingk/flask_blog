
from flask import Flask
from app.config import DevConfig
from views import views_app
from extensions import db


def create_app():
    app = Flask(__name__)
    # get config from config.py
    app.config.from_object(DevConfig)
    db.init_app(app)
    views_app(app)
    return app





if __name__ == '__main__':
    app = create_app()
    app.run()
    # pass