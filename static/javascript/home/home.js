import {ShowList} from '../shows/shows_react'
import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'


let JsonShowData = $.get('/shows/list_shows');

ReactDOM.render(<ShowList showData={JsonShowData}/>, document.getElementById('react_container'))