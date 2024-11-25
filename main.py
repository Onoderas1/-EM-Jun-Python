from typing import Optional

from library import Library

def main() -> None:
    """
    Основная функция, реализующая интерфейс командной строки.
    """
    library = Library()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книг")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Год издания должен быть числом.")
        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '3':
            title = input("Введите название книги для поиска (оставьте пустым для пропуска): ")
            author = input("Введите автора книги для поиска (оставьте пустым для пропуска): ")
            year_input = input("Введите год издания книги для поиска (оставьте пустым для пропуска): ")
            try:
                year: Optional[int] = int(year_input) if year_input else None
                results = library.search_books(title, author, year)
                library.display_books(results)
            except ValueError:
                print("Год издания должен быть числом.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.change_status(book_id, status)
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер от 1 до 6.")

if __name__ == "__main__":
    main()
