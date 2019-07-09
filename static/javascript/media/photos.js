import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";

$.get('/media/list_photos', function(data){
    ReactDOM.render(<PhotoList flierData={data}/>, document.getElementById('react_container'));
});

class Photo extends React.Component{
    render() {
        let artistDisplay;
        if(this.props.data.artist){
            artistDisplay = <div className={'col-xs-12 col-md-6'}>Artist: this.props.data.artist</div>
        }
        let showDisplay;
        if(this.props.data.show){
            showDisplay = <div className={'col-xs-12 col-md-6'}>Show: this.props.data.show</div>
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                {artistDisplay}
                {showDisplay}
                <div className={'col-md-12'}>
                    <hr/>
                </div>
            </div>
        )
    }
}


export class PhotoList extends React.Component{
    render(){
        let contents = [];
        for(const val in this.props.flierData){
            contents.push(
                <Photo data={this.props.flierData[val]} key={val}/>
            );
        }
        return(
            <div className='container'>
                {contents}
            </div>
        )
    }
}
