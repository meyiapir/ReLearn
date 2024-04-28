# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем все файлы из локальной папки в рабочую директорию контейнера
COPY . /app

# Устанавливаем необходимые пакеты
RUN pip install -r requirements.txt

# Открываем порт 8501, который использует Streamlit
EXPOSE 8501

# Команда для запуска Streamlit при старте контейнера
CMD ["streamlit", "run", "webui.py", "--server.port 8501", "--server.address 0.0.0.0"]
