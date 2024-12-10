
import os
from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE для вашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'announproject.settings')

app = Celery('announproject')

# Используйте строку из settings.py для конфигурации Celery.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузите задачи Celery из всех зарегистрированных приложений Django.
app.autodiscover_tasks()