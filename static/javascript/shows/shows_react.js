import React from 'react'
import ReactDOM from 'react-dom'
import {ArtistList} from '../music/artists_react'


class Show extends React.Component{
    render() {
        return (
            <div className={'row'}>
                <div className={'col-xs-12 col-sm-6 col-md-4 col-lg-3'}>
                    <ArtistList artistData={this.props.data.artists}/>
                </div>
            </div>
        )
    }
}


export class ShowList extends React.Component{
    render(){
        let contents = [];
        for(const show in this.props.showData){
            contents.push(
                <Show data={show}/>
            )
        }
        return(
            {contents}
        )
    }
}