import React, { useState, useEffect } from 'react'

function BookDetails({ book, onFavorite, onEditBook }) {
    const [isEditing, setIsEditing] = useState(false);
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [year, setYear] = useState('');

    useEffect(() => {
        if (book) {
            setTitle(book.title);
            setAuthor(book.author);
            setYear(book.year);
        }
    }, [book]);

    const handleEditSubmit = (e) => {
        e.preventDefault();
        onEditBook({ ...book, title, author, year: parseInt(year, 10) });
        setIsEditing(false);
    };


    if (!book) return <p>Selecione um livro para ver os detalhes</p>;

    return (
        <div>
            {isEditing ? (
                <form onSubmit={handleEditSubmit}>
                    <h3>Editando Livro</h3>
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
                
            ) : (
            <>
                <h3>Deatalhes do Livro</h3>
                <p><strong>Título:</strong> {book.title}</p>
                <p><strong>Autor:</strong> {book.author}</p>
                <p><strong>Ano:</strong> {book.year}</p>
                <button onClick={() => onFavorite(book)}>Favoritar</button>
                <button onClick={() => setIsEditing(true)} style={{ marginLeft: '10px'}}>Editar</button>
            </>
            )}
        </div>
    );
}

export default BookDetails;