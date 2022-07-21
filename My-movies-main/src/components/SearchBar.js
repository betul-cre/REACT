const SearchBar = ({ searchMovie }) => {
  const handleFormSumbit = (event) => {
    event.preventDefault();
  };
  return (
    <form onSubmit={handleFormSumbit}>
      <div className='row g-3 '>
        <div className='col-10'>
          <input
            onChange={searchMovie}
            type='text'
            className='form-control'
            placeholder='Search a movie'
          />
        </div>

        <div className='col-2'>
          <button
            type='button'
            className='btn btn-md btn-danger'
            style={{ float: 'float-right' }}
          >
            Add movie
          </button>
        </div>
      </div>
    </form>
  );
};

export default SearchBar;
