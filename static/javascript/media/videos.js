import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";
import {parseDate} from "../util/date";

$.get('/media/list_videos', function(data){
    ReactDOM.render(<VideoList flierData={data}/>, document.getElementById('react_container'));
});

class Video extends React.Component{
    render() {
        let dateDisplay;
        if(this.props.data.date){
            const date = parseDate(this.props.data.date);
            dateDisplay = <div className={'col-xs-12 col-md-6'}><h2>Date: {date}</h2></div>
        }
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay = <div className={'col-xs-12 col-md-6'}><h2>Artist: {this.props.data.artist}</h2></div>
        }
        let showDisplay;
        if(this.props.data.show){
            showDisplay = <div className={'col-xs-12 col-md-6'}><h2>Show: {this.props.data.show}</h2></div>
        }
        let youtubeUrl = "https://www.youtube.com/embed/";
        let youtube_ender = this.props.data.youtube_url.split('/')[this.props.data.youtube_url.split('/').length-1];
        if('=' in youtube_ender){
            youtube_ender = youtube_ender.split('=')[youtube_ender.split('=').length-1]
        }
        youtubeUrl = youtubeUrl + youtube_ender;
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <iframe width="560" height="315" src={youtubeUrl} frameBorder="0"
                            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                            allowFullScreen>

                    </iframe>
                </div>
                {dateDisplay}
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
        for(const val in this.props.flierData){
            contents.push(
                <Video data={this.props.flierData[val]} key={val}/>
            );
        }
        return(
            <div className='container'>
                {contents}
            </div>
        )
    }
}
