import React from 'react'
import ReactDOM from 'react-dom'


class Artist extends React.Component{
    render() {
        let link;
        if(this.props.data.bandcamp){
            link=<a href={this.props.data.bandcamp}>Bandcamp</a>;
        }
        else if(this.props.data.soundcloud){
            link=<a href={this.props.data.soundcloud}>Soundcloud</a>;
        }
        else if(this.props.data.youtube){
            link=<a href={this.props.data.youtube}>Youtube</a>;
        }
        return (
            <div className="row">
                <div className={'col-md-4'}>
                    {this.props.data.name}
                </div>
                <div className={'col-md-4'}>
                    {this.props.data.hometown}
                </div>
                <div className={'col-md-4'}>
                    {link}
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.description}
                    <hr/>
                </div>
            </div>
        )
    }
}


export class ArtistList extends React.Component{
    render(){
        let contents = [];
        let i = 0;
        for(const val in this.props.artistData){
            contents.push(
                <Artist data={this.props.artistData[val]} key={i}/>
            );
            i++;
        }
        return(
            <div className='container'>
                {contents}
            </div>
        )
    }
}