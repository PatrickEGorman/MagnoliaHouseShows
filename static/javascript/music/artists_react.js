import React from 'react'
import ReactDOM from 'react-dom'


class Artist extends React.Component{
    render() {
        return (
            <p>
                {this.props.data.name}
            </p>
        )
    }
}


export class ArtistList extends React.Component{
    render(){
        let contents = [];
        for(const artist in this.props.artistData){
            contents.push(
                <Artist data={artist}/>
            )
        }
        return(
            {contents}
        )
    }
}