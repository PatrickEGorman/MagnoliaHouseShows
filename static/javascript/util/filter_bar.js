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

        let display_fields =[];
        for(const key in this.props.data.display_fields){
            const display_field = this.props.data.display_fields[key];
            let display_name = display_field.name;
            if(display_field.display_name){
                display_name = display_field.display_name;
            }
            let id = "dropdown" + i.toString();
            let display_inside = [];
            display_inside.push(<a className="nav-link dropdown-toggle" href="#"  id={id} data-toggle="dropdown"
                                  aria-haspopup="true" aria-expanded="false" key={i}>{display_name}</a>
            );
            i++;
            let nav_options = [];
            for (const option_key in display_field.options) {
                if (display_field.options.hasOwnProperty(option_key)) {
                    let option = display_field.options[option_key];
                    if(!(option.name in this.state.display_fields)) {
                        this.state.display_fields[option.name] = option.default;
                    }
                    let show_hide = "Display: ";
                    if(this.state.display_fields[option.name]){
                        show_hide = "Hide: "
                    }
                    nav_options.push(<a className={"dropdown-item"} href="#"
                                        onClick={() => {
                                            this.state.display_fields[option.name] = !this.state.display_fields[option.name];
                                            this.setState(this.state);
                                        }}
                                        key={i}>{show_hide}{option.name}</a>);
                    i++;
                }
            }
            display_inside.push(<div className="dropdown-menu" aria-labelledby={id} key={i}>{nav_options}</div>)
            i++;
            display_fields.push(<li className="nav-item dropdown" key={i}>{display_inside}</li>);
            i++;
        }
        return(
            <nav className="navbar navbar-expand-md navbar-dark bg-dark">
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#filterNav"
                        aria-controls="filterNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"> </span>
                </button>
                <div className="navbar-collapse collapse" id="filterNav">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item"><a className="nav-link" >Filter {this.props.name}</a></li>
                        <li className="nav-item"><a className="nav-link" href="#"  onClick={() => {this.props.callback("")}}>Show All</a></li>
                        {nav_filters}
                    </ul>
                    <ul className="navbar-nav mr-5">
                        {display_fields}
                        <li className={"nav-item"}><a className={"nav-link"}>{this.props.name} Display</a></li>
                    </ul>
                </div>
            </nav>
        )
    }
}