import {ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


$.get('/shows/list_shows', function(data){
    ReactDOM.render(<ShowList data={data} isHomePage={true}/>, document.getElementById('react_container'));
});

