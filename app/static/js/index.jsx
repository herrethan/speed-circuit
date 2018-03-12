import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';


import {MDCRipple} from '@material/ripple';
const ripple = new MDCRipple(document.querySelector('.foo-button'));

console.log('eggs?')


ReactDOM.render(<App />, document.getElementById('content'));

