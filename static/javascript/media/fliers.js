import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {parseDate} from "../util/date";
import {ViewMore} from "../util/view_support";


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
        let dateDisplay;
        if(this.props.data.date){
            const date = parseDate(this.props.data.date);
            dateDisplay = <div className={'col-xs-12 col-md-6'}><h2>Date: {date}</h2></div>;
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                {dateDisplay}
                <div className={'col-md-12'}>
                    {this.props.data.caption}
                </div>
                <div className={'col-md-12'}>
                    <h2>{this.props.data.show}</h2>
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
