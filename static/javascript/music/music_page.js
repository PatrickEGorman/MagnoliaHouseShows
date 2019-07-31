import {ArtistFilter, ArtistList} from './artists_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


let num_artists = 0;
let filter;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))

function loadArtists(){
    num_artists += 10;
    let url = '/music/artist_list';
    if(filter){
        url += "?"+filter;
    }
    $.get(url, function(data){
        if(!filter){
            ReactDOM.render(<ArtistFilter data={data} callback={filtered_callback}/>, document.getElementById('filter_bar'))
        }
        ReactDOM.render(<ArtistList artistData={data} num_artists={num_artists} callback={loadArtists}/>,
            document.getElementById('react_container'));
    });
}


function filtered_callback(filter_setting){
    num_artists = 0;
    filter = filter_setting;
    loadArtists();
}

$.ready(loadArtists());