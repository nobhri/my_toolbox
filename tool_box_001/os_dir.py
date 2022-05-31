import os


print("current dirrectory is " + os.getcwd())

os.makedirs("./new_directory/",exist_ok = True)

os.chdir("./new_directory/")#change directory

os.makedirs("./sub_directory/",exist_ok = True)