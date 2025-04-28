from domain.task import Task
from infra.database import SessionLocal


class TaskService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_task(self, title, description):
        if not title or not title.strip():
            raise ValueError("O título da tarefa é obrigatório.")
        if not description or not description.strip():
            raise ValueError("A descrição da tarefa é obrigatória.")

        task = Task(title=title, description=description)
        self.db_session.add(task)
        self.db_session.commit()
        return task

    def get_tasks(self):
        return self.db_session.query(Task).all()


