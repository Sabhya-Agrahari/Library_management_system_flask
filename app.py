from flask import Flask, request, jsonify, abort 
from models import Book, Member
from database import books_db, members_db
from utils import generate_token, authenticate, paginate

app = Flask(__name__)

# Create some initial data
books_db.append(Book(1, "Book One", "Author A", 2020))
books_db.append(Book(2, "Book Two", "Author B", 2021))
members_db.append(Member(1, "John Doe", "john@example.com"))

# Route for registering a member (simulated)
@app.route('/register', methods=['POST'])
def register_member():
    data = request.get_json()
    new_member = Member(len(members_db) + 1, data['name'], data['email'])
    members_db.append(new_member)
    return jsonify({"message": "Member registered successfully!"}), 201

# Route for generating authentication token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    member = next((m for m in members_db if m.email == data['email']), None)
    if member:
        token = generate_token(member.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 400
# Root route
@app.route('/')
def home():
    return ( "Welcome to the Library Management System!")

# Route for adding a book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(len(books_db) + 1, data['title'], data['author'], data['year'])
    books_db.append(new_book)
    return jsonify(new_book.to_dict()), 201

# Route for fetching books with search and pagination
@app.route('/books', methods=['GET'])
def get_books():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        abort(403)

    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    filtered_books = books_db

    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.title.lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.author.lower()]

    paginated_books = paginate(filtered_books, page, per_page)
    return jsonify([book.to_dict() for book in paginated_books])

# Route for updating a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    token = request.headers.get('Authorization')
    if not authenticate(token):
        abort(403)

    data = request.get_json()
    book = next((book for book in books_db if book.id == id), None)

    if book:
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.year = data.get('year', book.year)
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404

# Route for deleting a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    token = request.headers.get('Authorization')
    if not authenticate(token):
        abort(403)

    book = next((book for book in books_db if book.id == id), None)
    if book:
        books_db.remove(book)
        return jsonify({"message": "Book deleted successfully!"})
    return jsonify({"error": "Book not found"}), 404

# Route for getting members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify([member.to_dict() for member in members_db])

if __name__ == '__main__':
    app.run(debug=True)
