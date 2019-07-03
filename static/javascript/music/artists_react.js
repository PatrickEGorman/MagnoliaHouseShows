import React from 'react'
import ReactDOM from 'react-dom'


class Artist extends React.Component{
    render() {
        let embed;
        let link;
        if(this.props.data.bandcampEmbedCode){
            embed = this.props.data.bandcampEmbedCode;
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
                    <h4>
                        {this.props.data.name}
                    </h4>
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
                    <br/>
                    {embed}
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