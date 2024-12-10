FROM python:3.8

# Установите зависимости
RUN pip install django celery

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt


# Скопируйте ваш код
COPY . /app
WORKDIR /app

EXPOSE 8000
# Запустите сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]