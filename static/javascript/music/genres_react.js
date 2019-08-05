import React from 'react'
import {ViewMore} from "../util/view_support";
import {ArtistList} from "./artists_react";
import {ShowList} from "../shows/shows_react";



export class Genre extends React.Component{
    render() {
        let show_list = [];
        for(const key in this.props.data.artist_set) {
            const artist = this.props.data.artist_set[key];
            for (const show_key in artist.show_set) {
                const show = artist.show_set[show_key];
                let included = false;
                for(const list_show_key in show_list){
                    const list_show = show_list[list_show_key];
                    if(show.id === list_show.id){
                        included=true;
                    }
                }
                if(!included){
                    show_list.push(show);
                }
            }
        }

        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <h2>
                        {this.props.data.name}
                    </h2>
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.description}
                </div>
                <div className={'col-xs-12 col-md-6'}>
                    <h4>
                        Artists:
                    </h4>
                    <br/>
                    <ArtistList artistData={this.props.data.artist_set} num_artists={this.props.num_artists}
                    callback={this.props.artist_callback}/>
                </div>
                <div className={'col-xs-12 col-md-6'}>
                    <h4>
                        Shows:
                    </h4>
                    <br/>
                    <ShowList data={show_list} num_shows={this.props.num_shows} callback={this.props.show_callback}/>
                </div>
            </div>
        )
    }
}


class ListGenre extends React.Component{
    render() {
        let artist_display_list = [];
        let show_organize_list = [];
        let show_display_list = [];
        let i = 0;
        for(const key in this.props.data.artist_set) {
            if(i >4){
                show_display_list.push(
                <li className="list-group-item" key={key}>
                    <a href={'/music/genre/' + this.props.data.id}>View More</a>
                </li>);
                break;
            }
            const artist = this.props.data.artist_set[key];
            artist_display_list.push(
                <li className="list-group-item" key={key}>
                    <a href={'/music/artist/' + artist.id}>{artist.name}</a>
                </li>
            );
            i++;
            for (const show_key in artist.show_set) {
                const show = artist.show_set[show_key];
                if (!(show_organize_list.includes(show))) {
                    show_organize_list.push(show);
                }
            }
        }
        let j = 0;
        for(const key in show_organize_list) {
            if(j >4){
                show_display_list.push(
                <li className="list-group-item" key={key}>
                    <a href={'/music/genre/' + this.props.data.id}>View More</a>
                </li>);
                break;
            }
            const show = show_organize_list[key];
            show_display_list.push(
                <li className="list-group-item" key={key}>
                    <a href={'/music/artist/' + show.id}>{show.name}</a>
                </li>
            );
            j++;
        }

        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <h2>
                        <a href={'/music/genre/'+this.props.data.id}>
                            {this.props.data.name}
                        </a>
                    </h2>
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.description}
                </div>
                <div className={'col-xs-12 col-md-6'}>
                    <h4>
                        Artists:
                    </h4>
                    <br/>
                    <ul className={"list-group"}>
                        {artist_display_list}
                    </ul>
                </div>
                <div className={'col-xs-12 col-md-6'}>
                    <h4>
                        Shows:
                    </h4>
                    <br/>
                    <ul className={"list-group"}>
                        {show_display_list}
                    </ul>
                </div>
            </div>
        )
    }
}


export class GenreList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.data){
            if(parseInt(val) >= this.props.num_genres){
                view_more = <ViewMore callback={this.props.callback}/>;
                break;
            }
            else {
                contents.push(
                    <ListGenre data={this.props.data[val]} key={val}/>
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
