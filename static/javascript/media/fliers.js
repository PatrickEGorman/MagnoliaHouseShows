import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";
import {Show} from "../shows/shows_react";
import {FlierList} from "./media_react";


let num_fliers = 1;
let past_shows = false;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))

function LoadFliers() {
    num_fliers += 10;
    $.get('/media/list_fliers?num_fliers='+num_fliers+"&past_shows="+past_shows, function (data) {
        ReactDOM.render(<FlierList data={data} num_fliers={num_fliers} callback={LoadFliers}
           togglePast={togglePastShows} past_shows={past_shows}/>, document.getElementById('react_container'));
    });
}

function togglePastShows(){
    past_shows = !past_shows;
    num_fliers = 1;
    LoadFliers();
}

$.ready(LoadFliers());
