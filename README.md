# -EM-Jun-Python

## Описание

Данное консольное приложение предназначено для управления библиотекой книг. Оно позволяет:

- **Добавлять книги**: пользователь вводит название, автора и год издания книги. Книга добавляется с уникальным ID и статусом **"в наличии"**.
- **Удалять книги**: удаление книги по её уникальному ID.
- **Искать книги**: поиск по названию, автору или году издания. Можно использовать любые комбинации этих параметров.
- **Отображать все книги**: выводит список всех книг с их подробной информацией.
- **Изменять статус книги**: изменение статуса книги на **"в наличии"** или **"выдана"** по её ID.

## Хранение данных

- Данные о книгах хранятся в файле `library.json` в формате JSON.
- При каждом изменении данные автоматически сохраняются.

## Как использовать приложение

1. **Запуск приложения**:

   ```bash
   python main.py
