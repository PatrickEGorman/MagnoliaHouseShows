import React from 'react'


export class FilterBar extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            display_fields:{}
        };
    }
    render(){
        let nav_filters = [];

        let i = 0;
        for(const key in this.props.data.filters){
            if(this.props.data.filters.hasOwnProperty(key)) {
                const filter = this.props.data.filters[key];
                let display_name = filter.name;
                if(filter.display_name){
                    display_name = filter.display_name;
                }
                let id = "dropdown" + i.toString();
                let filter_inside = [];
                filter_inside.push(<a className="nav-link dropdown-toggle" href="#"  id={id} data-toggle="dropdown"
                                      aria-haspopup="true" aria-expanded="false" key={i}>{display_name}</a>
                );
                i++;
                let nav_options = [];
                if(!filter.sort_function){
                    filter.options.sort(function(a, b){
                        return b.number - a.number;
                    })
                }
                else {
                    filter.options.sort(function(a, b){filter.sort_function(a, b)});
                }
                for (const option_key in filter.options) {
                    if (filter.options.hasOwnProperty(option_key)) {
                        let option = filter.options[option_key];
                        nav_options.push(<a className={"dropdown-item"} href="#" onClick={() => this.props.callback(filter.name+"="+option.value)}
                                            key={i}>{option.name} : {option.number}</a>);
                        i++;
                    }
                }
                filter_inside.push(<div className="dropdown-menu" aria-labelledby={id} key={i}>{nav_options}</div>)
                i++;
                nav_filters.push(<li className="nav-item dropdown" key={i}>{filter_inside}</li>);
                i++;
            }
        }
        return(
            <nav className="navbar navbar-expand-md navbar-dark bg-dark">
                <a className="navbar-brand text-light" >Filter {this.props.name}</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#filterNav"
                        aria-controls="filterNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"> </span>
                </button>
                <div className="navbar-collapse collapse" id="filterNav">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item"><a className="nav-link" href="#"  onClick={() => {this.props.callback("")}}>Show All</a></li>
                        {nav_filters}
                    </ul>
                </div>
            </nav>
        )
    }
}