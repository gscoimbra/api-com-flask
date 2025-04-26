from flask import Blueprint, request, jsonify
from usecases.task_service import TaskService
from flasgger.utils import swag_from

task_bp = Blueprint('task_bp', __name__)
task_service = TaskService()

@task_bp.route('/tasks', methods=['POST'])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'}
                },
                'required': ['title', 'description']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Tarefa criada com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'}
                }
            }
        }
    }
})
def create_task():
    data = request.json
    task = task_service.add_task(data['title'], data['description'])
    return jsonify({'title': task.title, 'description': task.description}), 201

@task_bp.route('/tasks', methods=['GET'])
@swag_from({
    'tags': ['Tasks'],
    'responses': {
        200: {
            'description': 'Lista de tarefas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'description': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_tasks():
    tasks = task_service.list_tasks()
    return jsonify([{'title': t.title, 'description': t.description} for t in tasks])
