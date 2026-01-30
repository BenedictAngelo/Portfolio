import os

file_path = "test/test.txt"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists")

    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("The file does not exist")
