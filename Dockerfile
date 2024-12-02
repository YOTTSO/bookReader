# Базовый образ Python
FROM python:3.12-slim


# Установка рабочего каталога
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt /app/

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . /app/

# Сборка статических файлов
RUN python manage.py collectstatic --noinput

# Экспонирование порта для Gunicorn
EXPOSE 8000

# Команда запуска
CMD ["gunicorn", "bookReader.wsgi:application", "--bind", "0.0.0.0:8000"]
