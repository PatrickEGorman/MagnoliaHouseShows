import {Show} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

let show_id_meta = document.getElementById('show_id');
const show_id = show_id_meta.content;

$.get('/shows/get_show/'+show_id, function(data){
    ReactDOM.render(<Show data={data}/>, document.getElementById('react_container'));
}).fail(ReactDOM.render(<h1>404 Show Not Found</h1>, document.getElementById('react_container')));

