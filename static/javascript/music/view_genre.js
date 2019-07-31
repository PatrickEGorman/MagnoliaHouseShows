import {Genre} from './genres_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

const genre_name_meta = document.getElementById('genre_id');
const genre_id = genre_name_meta.content;

$.get('/music/get_genre/'+genre_id, function(data){
    ReactDOM.render(<Genre data={data}/>, document.getElementById('react_container'));
});
