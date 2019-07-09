import React from 'react'
import ReactDOM from 'react-dom'
import $ from "jquery";

$.get('/media/list_fliers', function(data){
    ReactDOM.render(<FlierList flierData={data}/>, document.getElementById('react_container'));
});

class Flier extends React.Component{
    render() {
        let dateDisplay;
        if(this.props.data.date){
            dateDisplay = <div className={'col-xs-12 col-md-6'}><h2>Date: {this.props.data.date}</h2></div>;
        }
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    <img src={this.props.data.image} alt={this.props.data.caption}/>
                </div>
                {dateDisplay}
                <div className={'col-md-12'}>
                    {this.props.data.caption}
                </div>
                <div className={'col-md-12'}>
                    {this.props.data.show}
                </div>
                <div className={'col-md-12'}>
                    <hr/>
                </div>
            </div>
        )
    }
}


export class FlierList extends React.Component{
    render(){
        let contents = [];
        for(const val in this.props.flierData){
            contents.push(
                <Flier data={this.props.flierData[val]} key={val}/>
            );
        }
        return(
            <div className='container'>
                {contents}
            </div>
        )
    }
}
