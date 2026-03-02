# library.py
# This script creates a SQLite database named library.db
# It creates a table named 'books' and performs insert, select, update, and delete operations

import sqlite3

# Step 1: Connect to the database (it will create library.db if it doesn't exist)
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Step 2: Drop the books table if it already exists to avoid duplication
cursor.execute("DROP TABLE IF EXISTS books;")

# Step 3: Create the books table
cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT
);
""")

# Step 4: Insert the 10 specified books
books_data = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian Fiction"),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy"),
    ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, "Magical Realism"),
    ("The Hitchhikers Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction"),
    ("The Handmaids Tale", "Margaret Atwood", 1980, "Dystopian Fiction"),
    ("War and Peace", "Leo Tolstoy", 1869, "Fiction"),
    ("Ulysses", "James Joyce", 1922, "Fiction")
]

cursor.executemany("INSERT INTO books (title, author, publication_year, genre) VALUES (?, ?, ?, ?);", books_data)

# Step 5: Select all fiction books
cursor.execute("SELECT * FROM books WHERE genre='Fiction';")
fiction = cursor.fetchall()
print("All fiction books:", fiction)

# Step 6: Update The Handmaids Tale publication_year to 1985
cursor.execute("UPDATE books SET publication_year=1985 WHERE title='The Handmaids Tale';")
cursor.execute("SELECT * FROM books WHERE title='The Handmaids Tale';")
handmaids = cursor.fetchall()
print("Updated The Handmaids Tale:", handmaids)

# Step 7: Delete the book 1984
cursor.execute("DELETE FROM books WHERE title='1984';")

# Step 8: Print all books after deletion
cursor.execute("SELECT * FROM books;")
all_books = cursor.fetchall()
print("All books after deletion:", all_books)

# Step 9: Commit changes and close connection
connection.commit()
connection.close()# Right your code here
