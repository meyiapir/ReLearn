# ReLearn by `NOSTYLIST`

## Как запустить проект

### Предварительные требования
Для запуска проекта у вас должен быть установлен `Docker`.

### Клонирование репозитория
Склонируйте репозиторий проекта на свой локальный компьютер:

```bash
git clone https://github.com/meyiapir/ReLearn.git
cd your-repository-directory
```

### Сборка Docker образа
Соберите Docker образ из вашего Dockerfile:
```bash
docker build -t relearn-app .
```
### Запуск контейнера
Запустите контейнер из образа:
```bash
docker run -p 8501:8501 relearn-app
После запуска откройте веб-браузер и введите localhost:8501. Вы увидите интерфейс Streamlit, где можно загрузить файл CSV и обработать данные.
