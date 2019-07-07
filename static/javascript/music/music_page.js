import {ArtistList} from './artists_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


$.get('/music/artist_list', function(data){
    ReactDOM.render(<ArtistList artistData={data}/>, document.getElementById('react_container'));
});

