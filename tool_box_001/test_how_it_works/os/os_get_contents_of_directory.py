import os

dir_path = os.getcwd()

# get directory contents as a list
list_of_the_file_name_of_the_directory = os.listdir(dir_path)
print(list_of_the_file_name_of_the_directory)


# get directory contents as a list but only files
list_of_just_files = []
for file_or_directory_name in list_of_the_file_name_of_the_directory:
    # print(os.path.isfile(dir_path + file_or_directory_name))#return true if it is a file
    if os.path.isfile(file_or_directory_name):
        list_of_just_files.append(file_or_directory_name)
print(list_of_just_files)