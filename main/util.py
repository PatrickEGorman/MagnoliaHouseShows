import datetime


months = {1:"January", 2: "February", 3:"March", 4: "April", 5:"May", 6: "June", 7:"July", 8: "August",
    9:"September", 10: "October", 11:"November", 12: "December"};


def parse_date_string(date, year_month=False):
    if not date:
        return None
    split_date = date.__str__().split('-')
    now = datetime.datetime.now()
    this_year = now.year

    month = months[int(split_date[1])]
    day = int(split_date[2])
    year = int(split_date[0])
    if year_month:
        return [year, month]

    if year == this_year:
        return "%s %d" % (month, day)

    else:
        return "%s %d, %d" % (month, day, year)


priority_choices = [(1, "Minimum"),
                    (2, "Low"),
                    (3, "Average"),
                    (4, "High"),
                    (5, "Maxiumum")]