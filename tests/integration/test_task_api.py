# tests/integration/test_task_api.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_create_task(client):
    # Envia uma requisição POST para criar uma tarefa
    response = client.post('/tasks', json={
        'title': 'Tarefa de Integração',
        'description': 'Testar criação de tarefa via API'
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Tarefa de Integração'
    assert data['description'] == 'Testar criação de tarefa via API'

def test_get_tasks(client):
    # Envia uma requisição GET para listar as tarefas
    response = client.get('/tasks')

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Deve retornar uma lista
    assert any(task['title'] == 'Tarefa de Integração' for task in data)
