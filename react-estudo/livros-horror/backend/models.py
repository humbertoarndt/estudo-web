# ==============================================================================
# Imports
# ==============================================================================
from db import db

# ==============================================================================
# Class
# ==============================================================================
class Book(db.model):
    """
    Classe para modelar um objeto Book.

    Args:
        db (_type_): Conexão com bando de dados.
    """
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100), unique=True, nullable=False)
    author =db.Column(db.String(100), unique=False, nullable=False)
    year =db.Column(db.Integer(4), unique=False, nullable=False)


# ==============================================================================
# Functions
# ==============================================================================
def add_book(title: str, author: str, year: int) -> dict:
    """
    Função para adicionar um novo livro ao banco de dados.

    Args:
        title (str): Título do livro.
        author (str): Autor do livro.
        year (int): Ano de publicação do livro.

    Returns:
        dict: Em caso de erro mensagem informativa, em caso de sucesso registros
        inclusos no banoc de dados.
    """
    if not title:
        return {'message': 'Título não encontrado'}, 400
    elif not author:
        return {'message': 'Autor não encontrado'}, 400
    elif not year:
        return {'message': 'Ano não encontrado'}, 400
    else:
        existing_book = Book.query.filter_by(title=title).first()
        if existing_book:
            return {'message': 'Este livro já existe'}, 400

    new_book = Book(title=title, author=author, year=year)
    db.session.add(new_book)
    db.session.commit()
    return {'id': new_book.id, 'title': new_book.title, 'author': new_book.author, 'year': new_book.year}, 201


def get_books() -> list:
    """
    Função para listar livros em banco de dados.

    Returns:
        list: Lista de dicionários contendo os dados dos livros em banco de dados.
    """
    books = Book.query.all()
    return [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year} for book in books]


def update_book(book_id: int, new_tile: str, new_author: str, new_year: int) -> dict:
    """
    Função para atualizar um livro no banco de dados.

    Args:
        book_id (int): Id do livro em banco de dados.
        new_tile (str): Novo título.
        new_author (str): Novo autor.
        new_year (int): Novo ano de publicação.

    Returns:
        dict: Mensagem informativa para os casos de erro e de sucesso.
    """
    book = Book.query.get(book_id)
    if book:
        book.title = new_tile
        book.author = new_author
        book.year = new_year
        return {'message': 'Livro atualizado com sucesso'}, 200
    return {'message': 'Livro não encontrado'}, 404


def delete_book(book_id: int) -> dict:
    """
    Função para deletar um livro do banco de dados.

    Args:
        book_id (int): Id do livro em banco de dados.

    Returns:
        dict: Mensagem informativa para os casos de erro e de sucesso.
    """
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message:' 'Livro removido com sucesso'}, 200
    return {'message': 'Livro não encontrado'}, 404