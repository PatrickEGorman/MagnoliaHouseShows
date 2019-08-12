import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";
import {VideoList} from "./media_react";


let num_videos = 1;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))

function loadVideos(){
    num_videos += 10;
    $.get('/media/list_videos?num_videos='+num_videos, function(data){
        ReactDOM.render(<VideoList data={data} num_videos={num_videos} callback={loadVideos}/>, document.getElementById('react_container'));
    });
}

$.ready(loadVideos());
