import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {ViewMore} from "../util/view_support";


let num_videos = 1;

ReactDOM.render(<h1>Loading...</h1>, document.getElementById('react_container'))

function loadVideos(){
    num_videos += 10;
    $.get('/media/list_videos?num_videos='+num_videos, function(data){
        ReactDOM.render(<VideoList videoData={data}/>, document.getElementById('react_container'));
    });
}

$.ready(loadVideos());

class Video extends React.Component{
    render() {
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay =
                <div className={'col-xs-12 col-md-6'}>
                    <a href={'/music/artist/'+this.props.data.artist.id}><h2>Show: {this.props.data.artist.name}</h2></a>
                </div>
        }
        let showDisplay;
        if(this.props.data.show){
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
        for(const val in this.props.videoData){
            if(parseInt(val) === num_videos-1){
                view_more = <ViewMore callback={LoadVideos}/>
            }
            else {
                contents.push(
                    <Video data={this.props.videoData[val]} key={val}/>
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
