import React from 'react'
import {ArtistList} from '../music/artists_react'
import {ViewMore} from "../util/view_support";
import {FilterBar} from "../util/filter_bar";
import {months} from "../util/date";


export class Show extends React.Component{
    render() {
        let split_time = this.props.data.time.split(":");
        const hour = parseInt(split_time[0]);
        const minute = split_time[1];
        let facebook;
        let instagram;
        if(this.props.data.facebook) {
            facebook = <a href="this.props.data.facebook" target="_blank" className="fa fa-facebook"> </a>;
        }
        if(this.props.data.instagram){
            instagram =
                <a href = {this.props.data.instagram}
                    target = "_blank"
                    className = "fa fa-instagram" >
                </a>
        }
        let links=[];
        if(this.props.data.facebook){
            links.push(<a href={this.props.data.facebook} className={'btn bg-dark text-light'} key={1}>Facebook Event</a>);
        }
        if(this.props.data.instagram){
            links.push(<a href={this.props.data.instagram} className={'btn bg-dark text-light'} key={2}>Instagram Event</a>);
        }

        let donationMax;
        if(this.props.data.suggested_donation_max > this.props.data.suggested_donation){
            donationMax = "-"+this.props.data.suggested_donation_max;
        }

        if(this.props.data.fliers[0]){
            return(
                <div className={"container"}>
                    <div className={'row mb-3'}>
                        <div className={"col"}>
                            <h2>{this.props.data.date_string} {hour}:{minute}PM</h2> {facebook} {instagram}
                        </div>
                    </div>
                    <div className={'row mb-5'}>
                        <div className={'col-xs-12 col-sm-8'}>


                            <ArtistList artistData={this.props.data.artists}/>
                            <br/>
                            <h3>${this.props.data.suggested_donation}{donationMax} Suggested Donation</h3>
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
                            <h2>{this.props.data.date_string} {hour}:{minute}PM</h2>
                        </div>
                    </div>
                    <div className={'row mb-5'}>
                        <div className={'col-xs-12 col-sm-8'}>
                            <ArtistList artistData={this.props.data.artists}/>
                        </div>
                        <div className={'col-xs-12 col-sm-4'}>
                            <h3>${this.props.data.suggested_donation}{donationMax} Suggested Donation</h3>
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


class ListShow extends React.Component{
    render() {
        let artist_list = [];
        let genre_list = [];
        let divider;
        for(const key in this.props.data.artists){
            if(this.props.data.artists.hasOwnProperty(key)) {
                let artist = this.props.data.artists[key];
                artist_list.push(
                    <span key={key}>
                        {divider}
                        <a href={'/music/artist/' + artist.id}>
                            {artist.name}
                        </a>
                    </span>
                );
                for(const genre_key in artist.genres){
                    const genre = artist.genres[genre_key];
                    if(!(genre_list.includes(genre))){
                        genre_list.push(genre)
                    }
                }
                divider = " / ";
            }
        }
        let split_time = this.props.data.time.split(":");
        const hour = parseInt(split_time[0]);
        const minute = split_time[1];
        let genres = [];
        let genreDiv = "";
        let genre_divider = '';
        let i = 0;
        for(const genreKey in genre_list){
            const genre = genre_list[genreKey];
            if(i > 5){
                console.log("Show on "+this.props.data.date_string+"has more than 5 genres.  Terminating display")
                break;
            }
            genres.push(<span key={genreKey}>{genre_divider}<a href={'/music/genre/'+genre.id}>{genre.name}</a></span>);
            i++;
            genre_divider = ', '
        }
        if(genres.length>=1){
            genreDiv =
                <div className="col-md-12">
                    <div className={ ' ml-4'}>
                        Genres: <small>{genres}</small>
                    </div>
                </div>
        }

        let donationMax;
        if(this.props.data.suggested_donation_max > this.props.data.suggested_donation){
            donationMax = "-"+this.props.data.suggested_donation_max;
        }

        return(
            <div className={'row mt-3'}>
                <h2>
                    <div className={"col-md-12"}>
                        {this.props.data.date_string} : <small>{artist_list}</small>
                    </div>
                        {genreDiv}
                    <div className={"col-md-12"}>
                        <div className={ 'ml-4'}>
                            {hour}:{minute}<small> PM </small>
                            ${this.props.data.suggested_donation}{donationMax} <small>suggested donation  </small>
                            <br/>
                            <a href={'/shows/view_show/'+this.props.data.id}>
                                More Info
                            </a>
                        </div>
                    </div>
                </h2>
            </div>
        )
    }
}


export class ShowFilters extends React.Component{

    filter_data(){
        let dates = [];
        let genres = [];
        let artists = [];
        let hometowns = [];
        for(const val in this.props.data) {
            if (this.props.data.hasOwnProperty(val)) {
                const show = this.props.data[val];
                let included_date = false;
                for (let i = 0; i < dates.length; i++) {
                    if (dates[i].name[0] === show.year_month[0] && dates[i].name[1] === show.year_month[1]) {
                        dates[i].number++;
                        included_date = true;
                        break;
                    }
                }
                if (!included_date) {
                    const option = {name: show.year_month, number: 1, value: show.year_month[0]+"-"+show.year_month[1]};
                    dates.push(option);
                }
                let included_genre = false;
                for(const genreKey in show.genres) {
                    let genre = show.genres[genreKey];
                    for (let i = 0; i < genres.length; i++) {
                        if (genres[i].name === genre.name) {
                            genres[i].number++;
                            included_genre = true;
                            break;
                        }
                    }

                    if (!included_genre) {
                        const option = {name: genre.name, number: 1, value: genre.id};
                        genres.push(option);
                    }
                }
                let included_artist = false;
                for(const artistKey in show.artists) {
                    const artist = show.artists[artistKey];
                    for (let i = 0; i < artists.length; i++) {
                        if (artists[i].name === artist.name) {
                            artists[i].number++;
                            included_artist = true;
                            break;
                        }
                    }

                    if (!included_artist) {
                        const option = {name: artist.name, number: 1, value: artist.id};
                        artists.push(option);
                    }

                    let included_hometown = false;
                    if (artist.hometown) {
                        for (let i = 0; i < hometowns.length; i++) {
                            if (hometowns[i].name === artist.hometown) {
                                hometowns[i].number++;
                                included_hometown = true;
                                break;
                            }
                        }

                        if (!included_hometown) {
                            const option = {name: artist.hometown, number: 1, value: artist.hometown};
                            hometowns.push(option);
                        }
                    }
                }
            }
        }
        for(let i=0; i < dates.length; i++){
            dates[i].name = months[dates[i].name[1]] +" "+dates[i].name[0];
        }
        return {
            filters:
            [
                {
                    name: "Date",
                    options: dates,
                    sort_function: function(a, b){
                        const a_value_split = a.value.split("-");
                        const b_value_split = b.value.split("-");
                        if(a_value_split[0] !== b_value_split[0]){
                            return a_value_split[0] - b_value_split[0]
                        }
                        else{
                            return a_value_split[1] - b_value_split[1];
                        }
                    }
                },
                {
                    name: "Genre",
                    options: genres
                },
                {
                    name: "Artist",
                    options: artists
                },
                {
                    name: "Hometown",
                    display_name: "Artist Hometown",
                    options: hometowns
                }
            ]
        }
    }

    render(){
        return(
            <FilterBar data={this.filter_data()} callback={this.props.callback} name={"Shows"}/>
        )
    }
}


export class ShowList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.data){
            if(parseInt(val) >= this.props.num_shows){
                view_more = <ViewMore callback={this.props.callback}/>;
                break;
            }
            else {
                contents.push(
                    <ListShow data={this.props.data[val]} key={val}/>
                );
                }
            }
        return(
            <div>
                {contents}
                {view_more}
            </div>
        )
    }
}