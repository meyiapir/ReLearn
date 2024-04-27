import streamlit as st
import csv
from io import StringIO

# Класс для работы с CSV
class CSVIO:
    @staticmethod
    def read(file):
        comments = []
        text_file = StringIO(file.read().decode('utf-8'))
        reader = csv.reader(text_file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            if row:  # Проверяем, не пустая ли строка
                comments.append(row[0].strip())  # Предполагается, что комментарий - это первый элемент в строке
        return comments

    @staticmethod
    def write(content):
        si = StringIO()
        writer = csv.writer(si)
        writer.writerows([[item] for item in content])  # Оборачиваем каждый элемент в список
        return si.getvalue()

# Подключаем файл с функцией score (убедитесь, что функция доступна)
from libs.scorer import score

# Заголовок приложения
st.title('ReLearn by `NOSTYLIST`')

# Загрузка файла пользователем
uploaded_file = st.file_uploader("Загрузи файл с комментами, и давай их оценивать!", type=['csv'])

if uploaded_file is not None:
    # Чтение файла
    comments = CSVIO.read(uploaded_file)

    # Оцениваем комментарии
    scores = score(comments)

    # Подготавливаем данные для записи
    result_csv = CSVIO.write([f"{comment}: {scores[comment]}" for comment in scores])

    # Показываем обработанные данные
    st.write('Вот твои оценённые комментарии:')
    st.dataframe([[comment, scores[comment]] for comment in scores])

    # Ссылка на скачивание обработанного файла
    st.download_button(
        label="Нажми здесь, чтобы скачать результат!",
        data=result_csv,
        file_name='result.csv',
        mime='text/csv',
    )
