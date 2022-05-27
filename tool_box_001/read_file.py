# read_file.py

directory = './tool_box_001/'
file_name = 'test_open_file.txt'
file_path = directory + file_name

with open(file_path, "r", encoding = 'utf-8') as f:
    file_contents = f.read()
    print(file_contents)