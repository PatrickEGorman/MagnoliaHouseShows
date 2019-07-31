import {GenreList} from './genres_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


let num_genres = 0;

function loadGenres(){
    num_genres += 10;
    let url = '/music/genre_list';
    $.get(url, function(data){
        ReactDOM.render(<GenreList data={data} num_genres={num_genres} callback={loadGenres}/>,
            document.getElementById('react_container'));
    });
}

$.ready(loadGenres());