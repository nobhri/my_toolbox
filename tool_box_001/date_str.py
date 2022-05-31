import datetime

# get current date
current_date_as_date = datetime.date.today()
print(current_date_as_date)

# date to strings
current_date_as_str = current_date_as_date.strftime('%Y%m%d')
print(current_date_as_str)

input_str = '20220401'
parsed_str_as_date = datetime.datetime.strptime(input_str,'%Y%m%d')
print(parsed_str_as_date)