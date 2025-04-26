from celery import Celery

celery_app = Celery(
    'worker',
    broker='redis://localhost:6379/0',   # Redis está rodando localmente na porta 6379
    backend='redis://localhost:6379/0'
)

# IMPORTA AS TASKS AQUI 👇
import usecases.notification_service