import json
import os
from typing import List, Optional

from book import Book

class Library:
    """
    Класс для управления библиотекой книг.
    """

    def __init__(self, data_file: str = 'library.json') -> None:
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """
        Загружает книги из файла JSON.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(book) for book in books_data]
        else:
            self.books = []

    def save_books(self) -> None:
        """
        Сохраняет книги в файл JSON.
        """
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def generate_id(self) -> int:
        """
        Генерирует уникальный идентификатор для новой книги.
        """
        if self.books:
            return max(book.id for book in self.books) + 1
        else:
            return 1

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.
        """
        book_id = self.generate_id()
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга с ID {book_id} успешно добавлена.")

    def delete_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по ID.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Ищет книгу по ID.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, title: str = '', author: str = '', year: Optional[int] = None) -> List[Book]:
        """
        Ищет книги по названию, автору или году издания.
        """
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if year is not None:
            results = [book for book in results if book.year == year]
        return results

    def display_books(self, books: Optional[List[Book]] = None) -> None:
        """
        Отображает список книг.
        """
        if books is None:
            books = self.books
        if books:
            for book in books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
        else:
            print("Книг не найдено.")

    def change_status(self, book_id: int, status: str) -> None:
        """
        Изменяет статус книги по ID.
        """
        book = self.find_book_by_id(book_id)
        if book:
            if status in ["в наличии", "выдана"]:
                book.status = status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{status}'.")
            else:
                print("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
