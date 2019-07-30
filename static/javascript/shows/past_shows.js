import {ShowFilters, ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


let num_shows = 0;
let filter;

function reset_num_shows(){
    num_shows = 0;
}

function get_show_list() {
    num_shows += 10;
    let url ='/shows/list_shows?past_shows=True';
    if(filter){
        url += "&"+filter;
    }
    $.get(url, function (data) {
        if(!filter) {
            ReactDOM.render(<ShowFilters data={data}
                                         callback={filtered_callback}/>, document.getElementById('filter_bar'))
        }
        ReactDOM.render(<ShowList data={data} callback={get_show_list} num_shows={num_shows}
                                  reset_num_shows={reset_num_shows}/>, document.getElementById('react_container'));
    });
}

function filtered_callback(filter_setting){
    num_shows = 0;
    filter = filter_setting;
    get_show_list();
}


$.ready(get_show_list());
