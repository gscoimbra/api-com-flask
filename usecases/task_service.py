from domain.task import Task
from infra.database import SessionLocal

class TaskService:
    def __init__(self):
        self.db = SessionLocal()

    def add_task(self, title, description):
        task = Task(title, description)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_tasks(self):
        return self.db.query(Task).all()
