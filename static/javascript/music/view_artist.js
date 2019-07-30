import {Artist} from './artists_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

const artist_id_meta = document.getElementById('artist_id');
const artist_id = artist_id_meta.content;

$.get('/music/get_artist/'+artist_id, function(data){
    ReactDOM.render(<Artist data={data}/>, document.getElementById('react_container'));
});

