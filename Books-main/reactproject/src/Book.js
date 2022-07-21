import React from 'react';

const Book = ({ img, title, author }) => {
  const clickHandler = (e) => {
    console.log(e);
    console.log(e.target);
    alert('bought');
  };
  const complexExample = (author) => {
    console.log(author);
  };
  return (
    <article
      className='book'
      onMouseOver={() => {
        console.log(title);
      }}
    >
      <img src={img} alt='' />
      <h1 onClick={() => console.log(title)}>{title}</h1>
      <h5>{author}</h5>
      <button type='button' onClick={clickHandler}>
        Buy It
      </button>
      <button type='button' onClick={() => complexExample(author)}>
        Dont Buy
      </button>
    </article>
  );
};

export default Book;
