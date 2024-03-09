import os

# 1 Write a Python program to list only directories, files and all directories, files in a specified path.
def list_dir_files(path: str):
    print("Dir:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            print(i)
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
# list_dir_files(".")

# 2 Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check_access(path: str):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
# check_access(".")

# 3 Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def test_path(path: str):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")
# test_path("sample-data.json")

# 4 Write a Python program to count the number of lines in a text file.
def count_lines(filename: str):
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except:
        return 0
# print(count_lines("sample-data1.json"))

# 5 Write a Python program to write a list to a file.
def write_list_to_file(filename: str, lst: list):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(item + "\n")
    except:
        print("error")
# write_list_to_file("list.txt", ["apple"])

# 6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files():
    for letter in range(65, 91):
        with open(chr(letter) + ".txt", 'w') as file:
            file.write("This is file " + chr(letter) + ".txt")
# generate_files()

# 7 Write a Python program to copy the contents of a file to another file
def copy_file(src: str, dst: str):
    try:
        with open(src, 'r') as source, open(dst, 'w') as destination:
            destination.write(source.read())
    except:
        print("error")
# copy_file("source.txt", "destination.txt")

# 8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete_file(path: str):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File does not exist")
delete_file("delete.txt")
