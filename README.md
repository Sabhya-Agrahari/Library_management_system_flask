# Library_management_system_flask


A simple Flask application to manage books and members in a library. This API supports authentication, CRUD operations for books and members, and pagination.

## Features
- User authentication with token-based security
- Create, read, update, and delete books
- Create, read, update, and delete members
- Search and pagination for books

## Setup

1. Clone the repository:

    -bash
    git clone https://github.com/yourusername/library_management.git
    cd library_management
   

2. Set up a virtual environment (optional):

    -bash
    python -m venv venv
   

3. Activate the virtual environment:
   
       -bash
        venv\Scripts\activate
       
    

4. Install the dependencies:

    -bash
    pip install Flask
  

## Running the Application

1. Run the application with:

    -bash
    python app.py


    This will start the Flask development server at "http://127.0.0.1:5000/".

## API Endpoints

### Authentication
- **POST** '/login': Login with username and password to get a token.

### Books
- **GET** '/books': List books (supports search and pagination).
- **POST** '/books': Add a new book.
- **GET** '/books/{id}': Get details of a specific book.
- **PUT** '/books/{id}': Update a book.
- **DELETE** '/books/{id}': Delete a book.

### Members
- **GET** '/members': List members.
- **POST** '/members': Add a new member.
- **GET** '/members/{id}': Get details of a specific member.
- **PUT** '/members/{id}': Update a member.
- **DELETE** '/members/{id}': Delete a member.

## Example Usage

1. **Login:**

    -bash
    curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "password"}'
  

2. **Create a Book:**

    -bash
    curl -X POST http://127.0.0.1:5000/books -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"title": "New Book", "author": "Author Name", "year": 2024}'
   

3. **List Books:**

   -bash
    curl -X GET http://127.0.0.1:5000/books -H "Authorization: <token>"
  

## Using Postman

### 1. Login to Get a Token

1. **Method**: POST
2. **URL**: http://127.0.0.1:5000/login
3. **Body** (raw, JSON):
    '''json
    {
        "username": "admin",
        "password": "password"
    }
    '''  

4. **Response**:
  '''json
    {
        "token": "token-admin"
    }
    '''

### 2. Create a Book

1. **Method**: POST
2. **URL**: http://127.0.0.1:5000/books
3. **Headers**:
    '''
    Authorization: Bearer <your-token>
   '''
4. **Body** (raw, JSON):
    '''json
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    }
    '''

### 3. List Books

1. **Method**: GET
2. **URL**: http://127.0.0.1:5000/books
3. **Headers**:
    '''
    Authorization: Bearer <your-token>
   '''

### 4. Update a Book

1. **Method**: PUT
2. **URL**: http://127.0.0.1:5000/books/1
3. **Headers**:
    '''
    Authorization: Bearer <your-token>
    '''
4. **Body** (raw, JSON):
   '''json
    {
        "title": "The Great Gatsby (Updated)",
        "author": "F. Scott Fitzgerald",
        "year": 1926
    }
    '''

### 5. Delete a Book

1. **Method**: DELETE
2. **URL**: http://127.0.0.1:5000/books/1
3. **Headers**:
    '''
    Authorization: Bearer <your-token>
    ''''
