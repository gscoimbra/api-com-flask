from domain.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks
