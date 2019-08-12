import React from "react";
import {ViewMore} from "../util/view_support";

export class Video extends React.Component{
    render() {
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/music/artist/'+this.props.data.artist.id}><h2>Artist: {this.props.data.artist.name}</h2></a>
                </div>
        }
        let showDisplay;
        if((!(this.props.embed === "show")) && this.props.data.show){
            showDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/shows/view_show/'+this.props.data.show.id}><h2>Show: {this.props.data.show.name}</h2></a>
                </div>
        }
        let youtubeUrl = "https://www.youtube.com/embed/";
        let youtube_ender = this.props.data.youtube_url.split('/')[this.props.data.youtube_url.split('/').length-1];
        youtube_ender = youtube_ender.split('=')[youtube_ender.split('=').length-1]
        youtubeUrl = youtubeUrl + youtube_ender;
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <div className="video-responsive">
                        <iframe width="560" height="315" src={youtubeUrl} frameBorder="0"
                                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                                allowFullScreen>
                        </iframe>
                    </div>
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


export class VideoList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.data){
            if(parseInt(val) === this.props.num_videos){
                view_more = <ViewMore callback={this.props.callback} name={"Videos"}/>;
                break;
            }
            else {
                contents.push(
                    <Video data={this.props.data[val]} embed={this.props.embed} key={val}/>
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

export class Photo extends React.Component{
    render() {
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/music/artist/'+this.props.data.artist.id}><h2>Artist: {this.props.data.artist.name}</h2></a>
                </div>
        }
        let showDisplay;
        if((!(this.props.embed === "show")) && this.props.data.show){
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
        for(const val in this.props.data){
            if(parseInt(val) === this.props.num_photos){
                view_more = <ViewMore callback={this.props.callback} name={"Shows"}/>;
                break;
            }
            else {
                contents.push(
                    <Photo data={this.props.data[val]} embed={this.props.embed} key={val}/>
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


export class Flier extends React.Component{
    render() {
        let date;
        let show;
        if(!this.props.embed === "show"){
             date = <div className={'col-md-12'}>
                    {this.props.data.date_string}
                </div>;
            show = <div className={'col-md-12'}>
                    <h2><a href={'/shows/view_show/'+this.props.data.show.id}>{this.props.data.show.name}</a></h2>
                </div>;
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img className={"image"} src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                {date}
                <div className={'col-md-12'}>
                    {this.props.data.caption}
                </div>
                {show}
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
        if(this.props.past_shows){
            past_show_link = "Show Future Shows Fliers";
        }
        else{
            past_show_link = "Show Past Shows Fliers";
        }
        for(const val in this.props.data){
            if(parseInt(val) === this.props.num_fliers-1){
                view_more = <ViewMore callback={this.props.callback} name={"Fliers"}/>
            }
            else {
                contents.push(
                    <Flier data={this.props.data[val]} key={val}/>
                );
            }
        }
        return(
            <div className='container'>
                <div className={'row-md-12 mb-4'}>
                    <a className={'btn bg-dark text-light'} href="#" onClick={this.props.togglePast}>{past_show_link}</a>
                </div>
                {contents}
                {view_more}
            </div>
        )
    }
}
