from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/api-endpoints")
async def first_api(): 
    return {'message': 'Hello BachDuong'}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{item_id}")
async def read_a_book(item_id: int):
    return {**BOOKS[item_id]}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS: 
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Create a new book 
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
