import React, { useEffect, useState } from 'react';
import SearchBar from './SearchBar';
import MovieList from './MovieList';
import Data from './Data';
import axios from 'axios';
import Addmovie from './Addmovie';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

const App = () => {
  // useEffect(async () => {
  //   const baseURL = 'http://localhost:3002/movies';
  //   const response = await fetch(baseURL);
  //   console.log(response);
  //   const data = await response.json();
  //   console.log(data);
  //   setFilm(data);
  // }, []);

  useEffect(async () => {
    const response = await axios.get('http://localhost:3002/movies');
    console.log(response);
    setFilm(response.data);
  }, []);

  const [query, setQuery] = useState('');
  const searchMovie = (event) => {
    setQuery(event.target.value);
  };
  const [film, setFilm] = useState(Data);
  const removeFilm = (id) => {
    const newMovie = film.filter((films) => films.id !== id);

    setFilm(newMovie);
  };

  const AddMovie = async (movie) => {
    await axios.post('http://localhost:3002/movies', movie);
    setFilm(movie);
  };

  let filterMovies = film.filter((films) => {
    return films.name.toLowerCase().indexOf(query) !== -1;
  });
  return (
    <Router>
      <div className='container'>
        <Routes>
          <Route
            path='/'
            element={
              <React.Fragment>
                <div className='row'>
                  <div className='col-lg-12'>
                    <SearchBar searchMovie={searchMovie}></SearchBar>
                  </div>
                </div>

                <MovieList
                  film={filterMovies}
                  removeFilm={removeFilm}
                ></MovieList>
              </React.Fragment>
            }
          ></Route>
          <Route path='/add' element={<Addmovie />}></Route>
        </Routes>
      </div>
    </Router>
  );
};

{
}

export default App;
