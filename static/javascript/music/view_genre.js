import {Genre} from './genres_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

const genre_name_meta = document.getElementById('genre_id');
const genre_id = genre_name_meta.content;


let num_shows = 5;
let num_artists = 5;


function artist_callback(){
    num_artists+=5;
    get_genre();
}


function show_callback(){
    num_shows+=5;
    get_genre();
}



function get_genre() {
    $.get('/music/get_genre/' + genre_id, function (data) {
        ReactDOM.render(<Genre data={data} num_shows={num_shows} num_artists={num_artists}
            artist_callback={artist_callback} show_callback={show_callback}/>,
            document.getElementById('react_container'));
    });
}

$.ready(get_genre());
