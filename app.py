from flask import Flask
from interfaces.task_controller import task_bp
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

