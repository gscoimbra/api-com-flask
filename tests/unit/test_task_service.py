# tests/unit/test_task_service.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import pytest
from usecases.task_service import TaskService
from domain.task import Task


class FakeSession:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def commit(self):
        pass

    def close(self):
        pass


@pytest.fixture
def fake_session():
    return FakeSession()


@pytest.fixture
def task_service(fake_session):
    return TaskService(fake_session)


# Primeiro teste: criação válida
def test_create_task_success(task_service, fake_session):
    title = "Aprender Flask"
    description = "Criar API em Flask com Clean Architecture"

    task = task_service.create_task(title, description)

    assert task.title == title
    assert task.description == description
    assert len(fake_session.tasks) == 1


# Segundo teste: título inválido
def test_create_task_invalid_title(task_service):
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task("", "Descrição válida")

    assert str(exc_info.value) == "O título da tarefa é obrigatório."
