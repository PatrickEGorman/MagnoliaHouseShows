import React from 'react'
import ReactDOM from 'react-dom'


export class ViewMore extends React.Component(){
    constructor(){
        super();
        this.onClickCallback = this.props.callback;
    }
    render(){
        return(
            <div className={'col-md-12'}>
                <a className={'btn bg-dark text-light'} onClick={this.onClickCallback}>View More</a>
            </div>
        )
    }
}
