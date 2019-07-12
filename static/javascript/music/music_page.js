import {ArtistList} from './artists_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'
import {PhotoList} from "../media/photos";


let num_artists = 1;

function loadArtists(){
    num_artists += 10;
    $.get('/media/list_photos?num_artists='+num_artists, function(data){
        ReactDOM.render(<ArtistList artistData={data} num_artists={num_artists} callback={loadArtists}/>,
            document.getElementById('react_container'));
    });
}

$.ready(loadArtists());