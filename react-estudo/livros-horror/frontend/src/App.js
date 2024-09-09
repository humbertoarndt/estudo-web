import React, { useState, useEffect } from 'react';
// import Booklist from './components/BookList';
// import BookDetails from './components/BookDetails';
// import BookForm from './components/BookForm';
import './App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [newBook, setNewBook] = useState({ title: '', author: '', year: ''});
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    fetch('/books')
      .then(response => response.json())
      .then(data => setBooks(data))
      .catch(error => console.error('Erro ao buscar livros:', error));
  }, []);

  useEffect(() => {
    fetch('/favorites')
    .then(response => response.json())
    .then(data => setFavorites(data))
    .catch(error => console.error('Erro ao buscar favoritos:', error));
}, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewBook({ ...newBook, [name]: value });
  };

  const addFavorite = (bookId) => {
    fetch('/favorites', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ book_id: bookId }),
    })
    .then(response => response.json())
    .then(favorite => {
      if (!favorites.some(fav => fav.id === favorite.id)) {
        setFavorites([...favorites, favorite]);
      }
    })
    .catch(error => console.error('Erro ao adicionar favorito:', error));
  };

  const removeFavorite = (bookId) => {
    fetch(`/favorites/${bookId}`, {
      method: 'DELETE',
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'Book removed from favorites') {
          setFavorites(favorites.filter(fav => fav.id !== bookId));
        }
      })
      .catch(error => console.error('Erro ao remover favorito:', error));
  };

  // Adicionar livro
  const addBook = (book) => {
    fetch('/books', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(newBook),
    })
      .then(response => response.json())
      .then(newBook => setBooks([ ...books, newBook]));
  };

  return (
    <div className="App">
      <h1>Livros Clássicos de Horror</h1>

      <ul>
        {books.map(book => (
        <li key={book.id}>
          {book.title} - {book.author} ({book.year})
          <button onClick={() => addFavorite(book.id)}>Favoritar</button>
          </li>
        ))}
      </ul>

      <h2>Adicionar Novo Livro</h2>
        <input
            type="text"
            name='title'
            placeholder='Título'
            value={newBook.title}
            onChange={handleInputChange}
        />
        <input
            type="text"
            name='author'
            placeholder='Autor'
            value={newBook.author}
            onChange={handleInputChange}
        />
        <input
            type="number"
            name="year"
            placeholder='Ano'
            value={newBook.year}
            onChange={handleInputChange}
        />
        <button onClick={addBook}>Adicionar Livro</button>
        <h2>Livros Favoritos</h2>
        <ul>
          {favorites.map(book => (
            <li key={book.id}>
              {book.title} - {book.author} ({book.year})
              <button onClick={() => removeFavorite(book.id)}>Remover Favorito</button>
            </li>
          ))}
        </ul>
      </div>
  );
}

export default App;