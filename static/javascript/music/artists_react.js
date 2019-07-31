import React from 'react'
import {ViewMore} from "../util/view_support";
import {FilterBar} from "../util/filter_bar";


export class Artist extends React.Component{
    render() {
        let genres = [];
        let divider = '';
        let genreDiv = "";
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

        let embed = [];
        let links = [];
        let i = 0;
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
            links.push(<a href={this.props.data.bandcamp} key={i} className={'btn bg-dark text-light'}>Bandcamp</a>)
        }
        if(this.props.data.facebook){
            links.push(<a href={this.props.data.facebook} key={i} className={'btn bg-dark text-light'}>Facebook</a>)
        }
        if(this.props.data.soundcloud){
            links.push(<a href={this.props.data.soundcloud} key={i} className={'btn bg-dark text-light'}>Soundcloud</a>)
        }
        if(this.props.data.youtube){
            links.push(<a href={this.props.data.youtube} key={i} className={'btn bg-dark text-light'}>Youtube</a>)
        }
        let showList = [];
        if(this.props.data.show_set){
            let i = 0;
            showList.push(<div className={"col-md-12 mt-4"}><h4>Shows</h4></div> );
            i++;
            for(const key in this.props.data.show_set){
                const show = this.props.data.show_set[key];
                showList.push(
                    <div key={i} className={"col-md-12"}>
                        <a href={"/shows/view_show/"+show.id}>
                            {show.name}
                        </a>
                    </div>
                );
                i++;
            }
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
            </div>
        )
    }
}


class ListArtist extends React.Component{
    render() {
        let genres = [];
        let genreDiv = "";
        let divider = '';
        console.log(this.props.data.genres);
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
        let link;
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
        else if(this.props.data.bandcamp){
            link=<a href={this.props.data.bandcamp} className={'btn bg-dark text-light'}>Bandcamp</a>;
        }
        else if(this.props.data.soundcloud){
            link=<a href={this.props.data.soundcloud} className={'btn bg-dark text-light'}>Soundcloud</a>;
        }
        else if(this.props.data.youtube){
            link=<a href={this.props.data.youtube} className={'btn bg-dark text-light'}>Youtube</a>;
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
                    {link}
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
                view_more = <ViewMore callback={this.props.callback}/>;
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
