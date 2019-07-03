import {ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


$.get('/shows/list_shows', function(data){
    console.log(data);
    ReactDOM.render(<ShowList showData={data}/>, document.getElementById('react_container'));
});

