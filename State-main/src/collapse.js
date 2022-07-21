import React, { useEffect, useState } from 'react';

const Collapse = (props) => {
  const [state, setState] = useState(false);

  {
    return (
      <div>
        <button
          className='btn btn-primary w-100'
          onClick={() => setState(!state)}
        >
          {props.children.props.cardTitle}
        </button>
        {state ? (
          <div className='collapse show' id={props.href}>
            {props.children}
          </div>
        ) : (
          false
        )}
      </div>
    );
  }
};

export default Collapse;
