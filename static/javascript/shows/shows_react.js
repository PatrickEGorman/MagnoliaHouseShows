import React from 'react'
import ReactDOM from 'react-dom'
import {ArtistList} from '../music/artists_react'


class Show extends React.Component{
    render() {
        let split_date = this.props.data.date.split('-');
        const months = {1:"January", 2: "February", 3:"March", 4: "April", 5:"May", 6: "June", 7:"July", 8: "August",
            9:"September", 10: "October", 11:"November", 12: "December"};
        const month = months[parseInt(split_date[1])];
        const day = split_date[2];

        let split_time = this.props.data.time.split(":");
        const hour = parseInt(split_time[0]);
        const minute = split_time[1];

        let link;
        if(this.props.data.facebook){
            link=<a href={this.props.data.facebook} className={'btn bg-dark text-light'}>Facebook Event</a>;
        }
        return (
            <div className={'row mb-3'}>
                <div className={'col-xs-12 col-sm-7'}>
                    <h3>{month} {day}    {hour}:{minute}PM</h3>
                    <ArtistList artistData={this.props.data.artists}/>
                </div>
                <div className={'col-xs-12 col-sm-5'}>
                    <h3>${this.props.data.suggested_donation} Suggested Donation</h3>
                    {link}
                    <hr/>
                    <br/>
                    {this.props.data.description}
                    <br/>
                        {this.props.data.fliers[0].image}
                    <hr/>
                </div>
            </div>
        )
    }
}


export class ShowList extends React.Component{
    render(){
        let contents = [];
        let i = 0;
        for(const val in this.props.showData){
            contents.push(
                <Show data={this.props.showData[val]} key={i}/>
            );
            i++;
        }
        return(
            <div>
                {contents}
            </div>
        )
    }
}