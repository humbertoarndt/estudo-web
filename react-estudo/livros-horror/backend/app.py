# ==============================================================================
# Imports
# ==============================================================================
from flask import Flask, jsonify, request, send_from_directory

# ==============================================================================
# Global Variables
# ==============================================================================
app = Flask(__name__, static_folder="../frontend/build", static_url_path="")

books = [
    {'id': 1, 'title': 'Drácula', 'author': 'Bram Stocker', 'year': 1987},
    {'id': 2, 'title': 'Frankenstein', 'author': 'Mary Shelley', 'year': 1818},
    {'id': 3, 'title': 'O Médico e o Monstro', 'author': 'Robert Louis Steveson', 'year': 1886},
]

favorites = []

# ==============================================================================
# Routes
# ==============================================================================
@app.route('/books', methods=['GET'])
def get_books():
    """
    Função para listar os livros.

    Returns:
        Response: Livros existentes.
    """
    return jsonify(books), 200


@app.route('/books', methods=['POST'])
def add_book():
    """
    Função para adicionar um novo livro ao dicionário de livros.

    Returns:
        Response: Se não houver erros mensagem de sucesso, se não informativo de que
        livro já está listado ou aviso.
    """
    new_book = request.json
    title = new_book.get('title')

    if not title:
        return jsonify({'message': 'Título do livro é mandatório'})
    
    if any(book['title'].lower() == title.lower() for book in books):
        return jsonify({'message': 'Livro já listado'}), 409

    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    """
    Função para editar os valores de um livro.

    Args:
        book_id (int): Id do livro a ser editado.

    Returns:
        Response: Livro adicionado em caso de sucesso, ou mensagem de erro.
    """
    book_data = request.json
    for book in books:
        if book['id'] == book_id:
            book.update(book_data)
            return jsonify(book)
    return jsonify({'message': 'Livro não encontrado'}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Função para remover um livro.

    Args:
        book_id (int): Id do livro a ser removido.

    Returns:
        Response: Em caso de sucesso mensagem.
    """
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Livro excluído'}), 200


@app.route('/favorites', methods=['GET'])
def get_favorites():
    """
    Função para listar livros favoritos.

    Returns:
        Response: Livros favoritos.
    """
    return jsonify(favorites)


@app.route('/favorites', methods=['POST'])
def add_to_favorites():
    """
    Adiciona um livro novo aos favoritos se este livro ainda não estiver
    favoritado.

    Returns:
        Response: Se livro favoritado mensagem de sucesso, se livro já favoritado 
        mensagem informativa, em caso de erro mensagem.
    """
    book_id = request.json.get('book_id')
    book = next((book for book in books if book['id'] == book_id), None)
    if book and book not in favorites:
        favorites.append(book)
        return jsonify(book), 201
    elif book in favorites:
        return jsonify({'message': 'Livro já está nos favoritos'}), 400
    else:
        return jsonify({'message': 'Livro não encontrado'}), 404


@app.route('/favorites/<int:book_id>', methods=['DELETE'])
def remove_from_favorites(book_id):
    """
    Função para remover um livro da lista de favoritos.

    Args:
        book_id (int): Id do livro a ser removido dos favoritos.

    Returns:
        Response: Caso sucesso mensagem informando que livro foi removido, em caso de
        insucesso mensagem de erro.
    """
    global favorites
    book = next((book for book in favorites if book['id'] == book_id), None)
    if book:
        favorites = [fav for fav in favorites if fav['id'] != book_id]
        return jsonify({'message': 'Livro removido dos favoritos'}), 200
    else:
        return jsonify({'message': 'Livro não favoritado'}), 404


@app.route('/')
def serve():
    """
    Função para definir o ponto de entrada da aplicação React.

    Returns:
        Response: Arquivo 'index.html'
    """
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)