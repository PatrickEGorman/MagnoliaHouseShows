import {ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


$.get('/shows/list_shows?past_shows=True', function(data){
    ReactDOM.render(<ShowList showData={data} isHomePage={true}/>, document.getElementById('react_container'));
});

