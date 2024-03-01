#1
import os

def list_directories_and_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)
    
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

path = r"C:\Users\satyb\OneDrive\Рабочий стол\pp2"
list_directories_and_files(path)

#2
import os

def access(path):
    print("Existence:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))

path = r"C:\Users\satyb\OneDrive\Рабочий стол\pp2"
access(path)

#3
import os

def test_path_existence_and_split(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

path = r"C:\Users\satyb\OneDrive\Рабочий стол\pp2"
test_path_existence_and_split(path)

#4
def count(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

filename = r"C:\Users\satyb\OneDrive\Рабочий стол\pp2\lab6\example.txt"
lines = count(filename)
print("Number of lines in the file:", lines)

#5
def to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

my_list = [1, 2, 3, 4, 5]

file_name = "list21.txt"

to_file(my_list, file_name)

print(f"The list has been written to {file_name}.")

#6

import os

def generate_files(folder_path):
    for letter in range(65, 91):  
        filename = os.path.join(folder_path, chr(letter) + ".txt")
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

folder_path = r"C:\Users\satyb\OneDrive\Рабочий стол\pp2\fileletter"
generate_files(folder_path)
print("Text files created successfully.")

#7
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)


source_file = "example.txt"
destination_file = "list11.txt"

copy_file(source_file, destination_file)
print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")


#8
import os

def delete_file(file_path):
    
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist.")
        return
    
    if not os.access(file_path, os.R_OK | os.W_OK):
        print(f"You do not have permission to delete '{file_path}'.")
        return
    
    try:
        os.remove(file_path)
        print(f"The file '{file_path}' has been successfully deleted.")
    except Exception as e:
        print(f"An error occurred while deleting '{file_path}': {e}")

file_path = "list21.txt"

delete_file(file_path)

