import React from 'react'
import {ViewMore} from "../util/view_support";



class ListGenre extends React.Component{
    render() {
        return (
            <div className="row">
                <div className={'col-md-12'}>
                    {this.props.data.name}
                </div>
            </div>
        )
    }
}


export class GenreList extends React.Component{
    render(){
        let contents = [];
        let view_more;
        for(const val in this.props.data){
            if(parseInt(val) >= this.props.num_genres){
                view_more = <ViewMore callback={this.props.callback}/>;
                break;
            }
            else {
                contents.push(
                    <ListGenre data={this.props.data[val]} key={val}/>
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
