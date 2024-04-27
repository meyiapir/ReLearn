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
            if row:
                comments.append(row)
        return comments

    @staticmethod
    def write(content):
        si = StringIO()
        writer = csv.writer(si)
        writer.writerows([[item] for item in content])
        return si.getvalue()

from libs.scorer import score  # Предполагается, что функция score уже асинхронная

st.title('ReLearn by `NOSTYLIST`')

uploaded_file = st.file_uploader("Загрузи файл с комментами, и давай их оценивать!", type=['csv'])

if uploaded_file is not None:
    # Чтение файла
    comments = CSVIO.read(uploaded_file)
    comments = list(filter(lambda x: x[3] != "", comments))

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
