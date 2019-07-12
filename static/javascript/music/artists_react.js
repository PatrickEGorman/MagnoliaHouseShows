import React from 'react'
import ReactDOM from 'react-dom'
import {ViewMore} from "../util/view_support";


class Artist extends React.Component{
    render() {
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
            embed = <div className="col-md-12"
                                  dangerouslySetInnerHTML={htmlCode}/>
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
                    <h3>
                        {this.props.data.name}
                    </h3>
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


export class ArtistList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.artistData){
            if(parseInt(val) >= this.props.num_artists - 1){
                view_more = <ViewMore callback={this.props.callback}/>;
                break;
            }
            else {
                contents.push(
                    <Artist data={this.props.artistData[val]} key={val}/>
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
