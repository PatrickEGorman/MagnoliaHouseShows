import {ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


let num_shows = 1;


function get_show_list() {
    num_shows += 10;
    $.get('/shows/list_shows', function (data) {
        ReactDOM.render(<ShowList data={data} callback={get_show_list} num_shows={num_shows}/>, document.getElementById('react_container'));
    });
}

$.ready(get_show_list());
