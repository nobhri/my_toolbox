"""It prints formated datetime for mtg candidate date."""

from datetime import datetime, date, time, timedelta

datetime_list = [
    {
        "the_date": date(2023, 3, 6),
        "start_time": time(9, 30),
        "end_time": time(12, 0),
    },
    {
        "the_date": date(2023, 3, 6),
        "start_time": time(13, 0),
        "end_time": time(14, 0),
    },
    {
        "the_date": date(2023, 3, 7),
        "start_time": time(10, 30),
        "end_time": time(12, 0),
    },
]

for datetime_i in datetime_list:
    the_date = datetime_i["the_date"]
    start_time = datetime_i["start_time"]
    end_time = datetime_i["end_time"]
    print(
        "-",
        the_date.strftime("%m/%d(%a)"),
        start_time.strftime("%H:%M"),
        "~",
        end_time.strftime("%H:%M"),
    )
