import React from 'react';

const MovieList = ({ film, removeFilm }) => {
  return (
    <div className='row'>
      {film.map((films) => (
        <div className='col-lg-3' key={films.id}>
          <div className='card mb-4 shadow-sm'>
            <img src={films.imageURL} className='card-img rounded' alt='' />
            <div className='card-body'>
              <h5 className='card-title'> {films.name}</h5>
              <p className='card-text'>{films.overview}</p>
              <div className='d-flex justify-content-between align-items-center'>
                <button
                  type='button'
                  className='btn btn-md  btn-outline-danger '
                  onClick={() => removeFilm(films.id)}
                >
                  Delete
                </button>
                <h2>
                  <span>{film.rating}</span>
                </h2>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default MovieList;
