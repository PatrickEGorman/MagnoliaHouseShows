import react from 'react'
import reactDOM from 'react-dom'
import $ from 'jquery'

$(document).ready(function(){
    $("p").addClass("form-group");
    $("input").addClass("form-control");
    $("form > ul").addClass("list-group");
    $("ul.list-group > li").addClass("list-group-item");
});
