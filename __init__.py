from flask import Flask
from config import DevConfig


def create_app():
    app = Flask(__name__)
    # get config from config.py
    app.config.from_object(DevConfig)
    return app
app=create_app()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    pass