import React, { useState } from 'react';

function BookForm({ onAddBook }) {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [year, setYear] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (title && author && year) {
            onAddBook({ title, author, year: parseInt(year, 10)});
            setTitle('');
            setAuthor('');
            setYear('');
        } else {
            alert('Preencha todos os campos.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Adicionar Novo Livro</h2>
            <input
                type="text"
                placeholder='Título'
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="text"
                placeholder='Autor'
                value={author}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="number"
                placeholder='Ano'
                value={year}
                onChange={(e) => setTitle(e.target.value)}
            />
            <button type="submit">Adicionar Livro</button>
        </form>
    );
}

export default BookForm;