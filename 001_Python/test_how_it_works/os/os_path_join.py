import os

dir_path = os.getcwd()
sub_dir = 'sub_dir_for_test'
file_name = 'test.text'

# It works diffrently on each OS
joined_path = os.path.join(dir_path,sub_dir,file_name)
print(joined_path)


