import React from 'react'
import ReactDOM from 'react-dom'
import {ArtistList} from '../music/artists_react'


const months = {1:"January", 2: "February", 3:"March", 4: "April", 5:"May", 6: "June", 7:"July", 8: "August",
    9:"September", 10: "October", 11:"November", 12: "December"};


export class Show extends React.Component{
    render() {
        let split_date = this.props.data.date.split('-');

        const month = months[parseInt(split_date[1])];
        const day = split_date[2];

        let split_time = this.props.data.time.split(":");
        const hour = parseInt(split_time[0]);
        const minute = split_time[1];

        let links=[];
        if(this.props.data.facebook){
            links.push(<a href={this.props.data.facebook} className={'btn bg-dark text-light'} key={1}>Facebook Event</a>);
        }
        if(this.props.data.instagram){
            links.push(<a href={this.props.data.instagram} className={'btn bg-dark text-light'} key={2}>Instagram Event</a>);
        }
        if(this.props.data.fliers[0]){
            return(
                <div className={"container"}>
                    <div className={'row mb-3'}>
                        <div className={"col"}>
                            <h2>{month} {day} {hour}:{minute}PM</h2>
                        </div>
                    </div>
                    <div className={'row mb-5'}>
                        <div className={'col-xs-12 col-sm-8'}>


                            <ArtistList artistData={this.props.data.artists}/>
                            <br/>
                            <h3>${this.props.data.suggested_donation} Suggested Donation</h3>
                            {links}
                            <hr/>
                            <br/>
                            {this.props.data.description}
                            <hr/>
                        </div>
                        <div className={"col-xs-6 col-sm-4 mb-3"}>
                            <img src={this.props.data.fliers[0].image} className={"image"} alt={this.props.data.fliers[0].caption}/>
                            <br/>
                            {this.props.data.fliers[0].caption}
                            <hr/>
                        </div>
                    </div>
                </div>
            )
        }
        else {
            return (
                <div className={"container"}>
                    <div className={'row mb-3'}>
                        <div className={"col"}>
                            <h2>{month} {day} {hour}:{minute}PM</h2>
                        </div>
                    </div>
                    <div className={'row mb-5'}>
                        <div className={'col-xs-12 col-sm-8'}>
                            <ArtistList artistData={this.props.data.artists}/>
                        </div>
                        <div className={'col-xs-12 col-sm-4'}>
                            <h3>${this.props.data.suggested_donation} Suggested Donation</h3>
                            {links}
                            <hr/>
                            <br/>
                            {this.props.data.description}
                            <hr/>
                        </div>
                    </div>
                </div>
            )
        }
    }
}


class HomePageShow extends React.Component{
    render() {
        let split_date = this.props.data.date.split('-');

        const month = months[parseInt(split_date[1])];
        const day = split_date[2];
        let artists = '';
        for(const key in this.props.data.artists){
            artists += this.props.data.artists[key].name +" / ";
        }
        let split_time = this.props.data.time.split(":");
        const hour = parseInt(split_time[0]);
        const minute = split_time[1];
        let genres = "";
        let genreDiv = "";
        for(const genreKey in this.props.data.genres){
            if(genres.length>=1){
                genres+=", ";
            }
            genres += this.props.data.genres[genreKey].name;
        }
        if(genres.length>=1){
            genreDiv =
                <div className="col-md-12">
                    <div className={ ' ml-4'}>
                        Genres: <small>{genres}</small>
                    </div>
                </div>
        }
        return(
            <div className={'row mt-3'}>
                <h2>
                    <a href={'/shows/view_show/'+this.props.data.id}>
                        <div className={"col-md-12"}>
                            {month} {day} : <small>{artists.substring(0, artists.length-3)}</small>
                        </div>
                        {genreDiv}
                        <div className={"col-md-12"}>
                            <div className={ ' ml-4'}>
                                {hour}:{minute}<small> PM </small>
                                ${this.props.data.suggested_donation} <small>suggested donation  </small>
                            </div>
                        </div>
                    </a>
                </h2>
            </div>
        )
    }
}


export class ShowList extends React.Component{
    render(){
        let contents = [];
        for(const val in this.props.showData){
            contents.push(
                ((this.props.isHomePage)?
                    <HomePageShow data={this.props.showData[val]} key={val}/>:
                    <Show data={this.props.showData[val]}  key={val}/>
                )
            );
        }
        return(
            <div>
                {contents}
            </div>
        )
    }
}