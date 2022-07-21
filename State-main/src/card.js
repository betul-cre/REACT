import React from 'react';

const Card = (props) => {
  console.log(props);
  return (
    <div className='card w-100' style={{ width: '18rem' }}>
      <img src={props.image} className='card-img-top' alt='...' />
      <div className='card-body'>
        <p className='card-text'>{props.cardTitle}</p>
      </div>
    </div>
  );
};

export default Card;
