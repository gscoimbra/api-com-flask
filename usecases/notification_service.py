from infra.celery_worker import celery_app

@celery_app.task
def send_notification(task_title):
    print(f"[Celery] Enviando notificação: Tarefa '{task_title}' criada com sucesso!")
    return f"Notificação enviada para: {task_title}"
