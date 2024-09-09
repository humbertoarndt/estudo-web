import React from 'react';

function BookList({ books, onBookSelect, onDeleteBook }){
    return (
        <div>
            <h2>Lista de Livros Clássicos</h2>
            <ul>
                {books.map(book => (
                    <li key={book.id}>
                        <button onClick={() => onBookSelect(book)}>
                            {book.title} - {book.author}
                        </button>
                        <button onClick={() => onDeleteBook(book.id)} style={{ marginLeft: '10px'}}>
                            Excluir
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BookList;