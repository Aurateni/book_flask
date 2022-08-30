from reader.models import Book
from reader import db
import json

with open('books.json', encoding="utf8") as f:
    books_json = json.load(f)
    for book in books_json:
        book = Book(author=book['author'], description=book['description'], genre=book['genre'], rating=book['rating'],
                    title=book['title'], notes=book['notes'])
        db.session.add(book)
        db.session.commit()
