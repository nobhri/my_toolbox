# write_file.py

directory = './tool_box_001/'
file_name = 'test_written_file.txt'
file_path = directory + file_name
file_contents = 'hello'
with open(file_path, 'w', encoding = 'utf-8') as f:
    f.write(file_contents)
