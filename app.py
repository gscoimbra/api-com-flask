from flask import Flask
from interfaces.task_controller import create_task_blueprint


def create_app():
    app = Flask(__name__)

    task_bp = create_task_blueprint()
    app.register_blueprint(task_bp)

    return app
