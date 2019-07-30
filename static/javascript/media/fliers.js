import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";
import {Show} from "../shows/shows_react";


let num_fliers = 1;
let past_shows = false;


function LoadFliers() {
    num_fliers += 10;
    $.get('/media/list_fliers?num_fliers='+num_fliers+"&past_shows="+past_shows, function (data) {
        ReactDOM.render(<FlierList flierData={data}/>, document.getElementById('react_container'));
    });
}

function togglePastShows(){
    past_shows = !past_shows;
    num_fliers = 1;
    LoadFliers();
}

$.ready(LoadFliers());

class Flier extends React.Component{
    render() {
        console.log(this.props.data.show);
        this.state = {show_name: null};
        $.get('/shows/get_show/'+this.props.data.show, function(data){
            this.setState({show_name: data.name});
            console.log(data);
        }).fail(console.log("Failed!"));
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img className={"image"} src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.date_string}
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.caption}
                </div>
                <div className={'col-md-12'}>
                    <h2>{this.state.show_name}</h2>
                </div>
                <div className={'col-md-12'}>
                    <hr/>
                </div>
            </div>
        )
    }
}


export class FlierList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        let past_show_link;
        if(past_shows){
            past_show_link = "Show Future Shows Fliers";
        }
        else{
            past_show_link = "Show Past Shows Fliers";
        }
        for(const val in this.props.flierData){
            if(parseInt(val) === num_fliers-1){
                view_more = <ViewMore callback={LoadFliers}/>
            }
            else {
                contents.push(
                    <Flier data={this.props.flierData[val]} key={val}/>
                );
            }
        }
        return(
            <div className='container'>
                <div className={'row-md-12'}>
                    <a className={'btn bg-dark text-light'} href="#" onClick={togglePastShows}>{past_show_link}</a>
                </div>
                {contents}
                {view_more}
            </div>
        )
    }
}
