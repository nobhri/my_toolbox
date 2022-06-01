import os

# print(type(os.environ))
# os.environ has key and value

print(os.environ['PATH'])

# my environ variable as write on .profile
# export TEST_ENV="hello"
print(os.environ['TEST_ENV']) 
