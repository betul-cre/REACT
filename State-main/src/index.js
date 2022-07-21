import React from 'react';
import ReactDOM from 'react-dom';

import Card from './card';
import Collapse from './collapse';

const App = () => {
  return (
    <div className='container'>
      <div className='row'>
        <div className='card-group'>
          <div className='col'>
            <Collapse href='collapseExample1'>
              <Card
                cardTitle='Resim 1'
                image='https://picsum.photos/id/10/200/300'
              ></Card>
            </Collapse>
          </div>
          <div className='col'>
            <Collapse href='collapseExample2'>
              <Card
                cardTitle='Resim 2'
                image='https://picsum.photos/id/15/200/300'
              ></Card>
            </Collapse>
          </div>
          <div className='col'>
            <Collapse href='collapseExample3'>
              <Card
                cardTitle='Resim 3'
                image='https://picsum.photos/id/25/200/300'
              ></Card>
            </Collapse>
          </div>
        </div>
      </div>
    </div>
  );
};

ReactDOM.render(<App></App>, document.getElementById('root'));
