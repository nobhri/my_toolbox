import re

strings_list = ['20220601', '20220501','2022-05-01','hello']
pattern = '[0-9]{8}'
checker = re.compile(pattern)

for strings_i in strings_list:
    # strings_i = strings_list[0]
    result= checker.match(strings_i)
    print(bool(result))


# True
# True
# False
# False