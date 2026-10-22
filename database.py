
import sqlite3


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    conn.commit()


def insert_books(conn, name, author, publication_year, genre,
                 number_of_pages, number_of_copies):
    conn.execute("""
        INSERT INTO books (
            name, author, publication_year, genre,
            number_of_pages, number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name, author, publication_year, genre,
        number_of_pages, number_of_copies
    ))
    conn.commit()


def get_books_by_author(conn, author):
    cursor = conn.execute(
        "SELECT * FROM books WHERE author = ?",
        (author,)
    )
    return cursor.fetchall()


def delete_book_by_id(conn, book_id):
    conn.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    conn.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("database_v8.db")

    try:
        create_table(connection)

        cursor = connection.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]

        if count == 0:
            insert_books(connection, "Гарри Поттер", "Джоан Роулинг", 1997, "Фэнтези", 350, 5)
            insert_books(connection, "Властелин колец", "Джон Толкин", 1954, "Фэнтези", 500, 3)
            insert_books(connection, "Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 480, 4)
            insert_books(connection, "Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 600, 2)
            insert_books(connection, "Война и мир", "Лев Толстой", 1869, "Роман", 1200, 3)
            insert_books(connection, "1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 6)
            insert_books(connection, "Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 4)
            insert_books(connection, "Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", 320, 3)
            insert_books(connection, "Три мушкетёра", "Александр Дюма", 1844, "Приключения", 700, 2)
            insert_books(connection, "Алиса в Стране чудес", "Льюис Кэрролл", 1865, "Сказка", 150, 5)

        print("Книги Джоан Роулинг:")
        books = get_books_by_author(connection, "Джоан Роулинг")

        for book in books:
            print(book)

        cursor = connection.execute("SELECT COUNT(*) FROM books")
        print("Всего книг в базе:", cursor.fetchone()[0])

    finally:
        connection.close()
