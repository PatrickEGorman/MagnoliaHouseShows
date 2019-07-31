import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";


let num_photos = 1;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))


function loadPhotos(){
    num_photos += 10;
    $.get('/media/list_photos?num_photos='+num_photos, function(data){
        ReactDOM.render(<PhotoList photoData={data}/>, document.getElementById('react_container'));
    });
}

$.ready(loadPhotos());


class Photo extends React.Component{
    render() {
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/music/artist/'+this.props.data.artist.id}><h2>Artist: {this.props.data.artist.name}</h2></a>
                </div>
        }
        let showDisplay;
        if(this.props.data.show){
            showDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/shows/view_show/'+this.props.data.show.id}><h2>Show: {this.props.data.show.name}</h2></a>
                </div>
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img className={'image'} src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.caption}
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.date_string}
                </div>
                {artistDisplay}
                {showDisplay}
                <div className={'col-md-12'}>
                    <hr/>
                </div>
            </div>
        )
    }
}


export class PhotoList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.photoData){
            if(parseInt(val) === num_photos-1){
                view_more = <ViewMore callback={LoadPhotos}/>
            }
            else {
                contents.push(
                    <Photo data={this.props.photoData[val]} key={val}/>
                );
            }
        }
        return(
            <div className='container'>
                {contents}
                {view_more}
            </div>
        )
    }
}
