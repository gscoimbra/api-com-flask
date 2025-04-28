from flask import Blueprint, request, jsonify
from infra.database import SessionLocal
from usecases.task_service import TaskService

def create_task_blueprint():
    task_bp = Blueprint('task_bp', __name__)

    @task_bp.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')

        service = TaskService(SessionLocal())
        task = service.create_task(title, description)

        return jsonify({
            "id": task.id,
            "title": task.title,
            "description": task.description
        }), 201

    @task_bp.route('/tasks', methods=['GET'])
    def list_tasks():
        service = TaskService(SessionLocal())
        tasks = service.get_tasks()

        return jsonify([{'title': t.title, 'description': t.description} for t in tasks])

    return task_bp
