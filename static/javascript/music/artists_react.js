import React from 'react'
import {ViewMore} from "../util/view_support";
import {FilterBar} from "../util/filter_bar";
import {FlierList, PhotoList, VideoList} from "../media/media_react";


export class Artist extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            num_photos: 3,
            num_videos: 2,
            num_fliers: 3
        }
    }

    render() {
        let genres = [];
        let divider = '';
        let genreDiv = "";
        let i = 0;
        for(const genreKey in this.props.data.genres){
            const genre = this.props.data.genres[genreKey];
            genres.push(<span key={i}>{divider}<a key={i} href={'/music/genre/'+genre.id}>{genre.name}</a></span>);
            divider=", ";
            i++;
        }
        if(genres.length>=1){
            genreDiv =
                <div className="col-md-12">
                    <h4>Genres: <small>{genres}</small> </h4>
                </div>
        }

        let embed = [];
        let links = [];
        if(this.props.data.bandcamp_embed_code)
        {
            const htmlCode = {__html: this.props.data.bandcamp_embed_code};
            embed.push(<div className="col-md-12" key={i}
                                  dangerouslySetInnerHTML={htmlCode}/>)
            i++;
        }
        if(this.props.data.soundcloud_embed_code){
            const htmlCode = {__html: this.props.data.soundcloud_embed_code };
            embed.push(<div className="col-md-12" key={i}
                                  dangerouslySetInnerHTML={htmlCode}/>)
            i++;
        }
        if(this.props.data.youtube_embed_code){
            const htmlCode = {__html: this.props.data.youtube_embed_code };
            embed.push(<div className="col-md-12" key={i}
                                  dangerouslySetInnerHTML={htmlCode}/>)
            i++;
        }
        if(this.props.data.bandcamp){
            links.push(<a href={this.props.data.bandcamp} key={i} className={'fa fa-bandcamp'}> </a>);
            i++;
        }
        if(this.props.data.facebook){
            links.push(<a href={this.props.data.facebook} key={i} target="_blank" className="fa fa-facebook"> </a>);
            i++;
        }
        if(this.props.data.soundcloud){
            links.push(<a href={this.props.data.soundcloud} key={i} className={'fa fa-soundcloud'}> </a>);
            i++;
        }
        if(this.props.data.youtube){
            links.push(<a href={this.props.data.youtube} key={i} className={'fa fa-youtube'}> </a>);
            i++;
        }
        let showList = [];
        let flierList = [];
        if(this.props.data.show_set){
            showList.push(<div key={i} className={"col-md-12 mt-4"}><h4>Shows</h4></div> );
            i++;
            for(const key in this.props.data.show_set){
                const show = this.props.data.show_set[key];
                if(show.flier){
                    let flier = show.flier;
                    flier.show = show;
                    flierList.push(flier);
                }
                showList.push(
                    <div key={i} className={"col-md-12"}>
                        <a key={i} href={"/shows/view_show/"+show.id}>
                            {show.name}
                        </a>
                    </div>
                );
                i++;
            }
        }
        let videos = [];
        if(this.props.data.videos.length>=1){
            videos[0] = <h2 key={i}>Videos</h2>;
            i++;
            videos.push(<VideoList data={this.props.data.videos} num_videos={this.state.num_videos} embed={"artist"}
                                   callback={()=>{
                                       this.state.num_videos+=5;
                                       this.setState(this.state);
                                   }} key={i}/>);
            i++;
            videos.push(<hr key={i}/>);
            i++;
        }

        let photos = [];
        if(this.props.data.photos.length>=1) {
            photos[0] = <h2 key={i}>Photos</h2>;
            i++;
            photos.push(<PhotoList data={this.props.data.photos} num_photos={this.state.num_photos} embed={"artist"}
                                   callback={()=>{
                                       this.state.num_photos+=5;
                                       this.setState(this.state);
                                   }} key={i}/>);
            i++;
            photos.push(<hr key={i}/>);
            i++;
        }

        let fliers = [];
        if(flierList.length>=1) {
            fliers[0] = <h2 key={i}>Fliers</h2>;
            i++;
            fliers.push(<FlierList data={flierList} num_photos={this.state.num_fliers}
                                   callback={()=>{
                                       this.state.num_fliers+=5;
                                       this.setState(this.state);
                                   }} embed={'artist'} key={i}/>);
            i++;
            fliers.push(<hr key={i}/>);
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <h1>
                        {this.props.data.name}
                    </h1>
                </div>
                <br/>
                <div className={'col-md-12'}>
                    <h3>
                        {this.props.data.hometown}
                    </h3>
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.description}
                </div>
                {genreDiv}
                {embed}
                <div className={'col-md-12'}>
                    {links}
                </div>
                {showList}
                {videos}
                {photos}
                {fliers}
            </div>
        )
    }
}


class ListArtist extends React.Component{
    render() {
        let genres = [];
        let genreDiv = "";
        let divider = '';
        for(const genreKey in this.props.data.genres){
            const genre = this.props.data.genres[genreKey];
            genres.push(<span key={genreKey}>{divider}<a href={'/music/genre/'+genre.id}>{genre.name}</a></span>);
            divider=", ";
        }
        if(genres.length>=1){
            genreDiv =
                <div className="col-md-12">
                    <h4>Genres: <small>{genres}</small> </h4>
                </div>
        }

        let embed;
        let links = [];
        let i = 0;
        if(this.props.data.bandcamp_embed_code)
        {
            const htmlCode = {__html: this.props.data.bandcamp_embed_code};
            embed = <div className="col-md-12"
                                  dangerouslySetInnerHTML={htmlCode}/>
        }
        else if(this.props.data.soundcloud_embed_code){
            const htmlCode = {__html: this.props.data.soundcloud_embed_code };
            embed = <div className="col-md-12"
                                  dangerouslySetInnerHTML={htmlCode}/>
        }
        else if(this.props.data.youtube_embed_code){
            const htmlCode = {__html: this.props.data.youtube_embed_code };
            embed = <div className="col-md-6"><div className="video-responsive"
                                                   dangerouslySetInnerHTML={htmlCode}/></div>
        }
        if(this.props.data.bandcamp){
            links.push(<a key={i} href={this.props.data.bandcamp} className={'fa fa-bandcamp'}> </a>);
            i++;
        }
        if(this.props.data.facebook){
            links.push(<a href={this.props.data.facebook} key={i} target="_blank" className="fa fa-facebook"> </a>);
            i++;
        }
        if(this.props.data.soundcloud){
            links.push(<a key={i} href={this.props.data.soundcloud} className={'fa fa-soundcloud'}> </a>);
            i++;
        }
        if(this.props.data.youtube){
            links.push(<a key={i} href={this.props.data.youtube} className={'fa fa-youtube'}> </a>);
            i++;
        }
        return (
            <div className="row">
                <div className={'col-md-4'}>
                    <a href={'/music/artist/'+ this.props.data.id}>
                        <h3>
                            {this.props.data.name}
                        </h3>
                    </a>
                </div>
                <div className={'col-md-4'}>
                    <h4>
                        {this.props.data.hometown}
                    </h4>
                </div>
                <div className={'col-md-4'}>
                    {links}
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.description}
                </div>
                {genreDiv}
                {embed}
                <div className={'col-md-12'}>
                    <hr/>
                </div>
            </div>
        )
    }
}


export class ArtistFilter extends React.Component{
    
    filter_data(){
        let genres = [];
        let hometown = [];
        let embed_code = [
            {
                name: "Bandcamp",
                number: 0,
                value:"bandcamp"
            },
            {
                name: "Soundcloud",
                number: 0,
                value:"soundcloud"
            },
            {
                name: "Youtube",
                number: 0,
                value:"youtube"
            }];
        let social_media = [
            {
                name: "Bandcamp",
                number: 0,
                value:"bandcamp"
            },
            {
                name: "Facebook",
                number: 0,
                value:"facebook"
            },
            {
                name: "Soundcloud",
                number: 0,
                value:"soundcloud"
            },
            {
                name: "Youtube",
                number: 0,
                value:"youtube"
            }];

        for(const val in this.props.data) {
            if (this.props.data.hasOwnProperty(val)) {
                const artist = this.props.data[val];
                let included_genre = false;
                for(const genreKey in artist.genres) {
                    let genre = artist.genres[genreKey];
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
                let included_hometown = false;
                if (artist.hometown) {
                    for (let i = 0; i < hometown.length; i++) {
                        if (hometown[i].name === artist.hometown) {
                            hometown[i].number++;
                            included_hometown = true;
                            break;
                        }
                    }

                    if (!included_hometown) {
                        const option = {name: artist.hometown, number: 1, value: artist.hometown};
                        hometown.push(option);
                    }
                }
                if(artist.facebook){
                    social_media[1].number++;
                }
                if(artist.bandcamp_embed_code){
                    embed_code[0].number++;
                    social_media[0].number++;
                }
                else if(artist.bandcamp){
                    social_media[0].number++;
                }
                if(artist.soundcloud_embed_code){
                    embed_code[1].number++;
                    social_media[2].number++;
                }
                else if(artist.soundcloud){
                    social_media[2].number++;
                }
                if(artist.youtube_embed_code){
                    embed_code[2].number++;
                    social_media[3].number++;
                }
                else if(artist.youtube){
                    social_media[3].number++;
                }
            }
        }
        return {filters:
            [
                {
                    name: "Genre",
                    options: genres
                },
                {
                    name: "Hometown",
                    options: hometown
                },
                {
                    name: "Social",
                    display_name: "Social Media",
                    options: social_media
                },{
                    name: "Embed",
                    display_name: "Embed Code",
                    options: embed_code
                }
            ]
        }
    }

    render(){
        return(
            <FilterBar data={this.filter_data()} callback={this.props.callback} name={"Artists"}/>
        )
    }
}


export class ArtistList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.artistData){
            if(parseInt(val) >= this.props.num_artists){
                view_more = <ViewMore callback={this.props.callback}  name={"Artists"}/>;
                break;
            }
            else {
                contents.push(
                    <ListArtist data={this.props.artistData[val]} key={val}/>
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
