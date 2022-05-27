import datetime

# get current date
current_date_as_date = datetime.date.today()
print(current_date_as_date)

# date to strings
current_date_as_str = current_date_as_date.strftime('%Y%m%d')
print(current_date_as_str)