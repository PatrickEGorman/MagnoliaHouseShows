import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";
import {PhotoList} from "./media_react";


let num_photos = 1;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))


function loadPhotos(){
    num_photos += 10;
    $.get('/media/list_photos?num_photos='+num_photos, function(data){
        ReactDOM.render(<PhotoList data={data} num_photos={num_photos} callback={loadPhotos}/>, document.getElementById('react_container'));
    });
}

$.ready(loadPhotos());
