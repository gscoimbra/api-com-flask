from flask import Blueprint, request, jsonify
from usecases.task_service import TaskService

task_bp = Blueprint('task_bp', __name__)
task_service = TaskService()

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = task_service.add_task(data['title'], data['description'])
    return jsonify({'title': task.title, 'description': task.description}), 201

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_service.list_tasks()
    return jsonify([{'title': t.title, 'description': t.description} for t in tasks])
