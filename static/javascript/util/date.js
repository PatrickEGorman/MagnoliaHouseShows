exports.months = {1:"January", 2: "February", 3:"March", 4: "April", 5:"May", 6: "June", 7:"July", 8: "August",
    9:"September", 10: "October", 11:"November", 12: "December"};

exports.parseDate = function(date){
    let split_date = date.split('-');

    const currentDate = new Date();
    const current_year = currentDate.getFullYear();

    const month = months[parseInt(split_date[1])];
    const day = split_date[2];
    const year = split_date[0];

    if(parseInt(year)!==current_year){
        return month + " " + day + ", " + year;
    }
    else {
        return month + " " + day;
    }
};