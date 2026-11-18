# File handling project
#file = open("Sample.txt",'r')
#contents = file.read()


import os
from logging import exception

from prometheus_client.samples import Sample


def create_file(filename):
    try:

        with open(filename,'x') as f:
           print(f"File as  created with {filename} successfully")
    except FileExistsError:
        print(f"File {filename} already exists")
    except Exception as e:
        print("An error occured")

def view_file():
     files = os.listdir()
     if not files:
        print("File does not exist")
     else:
        print("File in directory ")
        for file in files:
            print(file)
def delete_file(filename):
     try:
         os.remove(filename)
         print(f"File {filename} deleted")
     except FileNotFoundError:
         print(f"File {filename} does not exist")
     except Exception as e:
         print("An error occured")

def read_file(filename):
     try:
         with open(Sample.txt,'r') as f:
           content = f.read()
           print(f"File as  read from '{filename}' :\n{content} successfully")
     except FileNotFoundError:
         print(f"File {filename} does not exist")
     except Exception as e:
         print("An error occured")
def edit_file(filename):
     try:
         with open(Sample.txt,'a') as f:
             content = input("Enter new line add content into file : ")
             f.write(content + "\n")
             print(f"File as  edited from '{filename}' successfully")
     except FileNotFoundError:
         print(f"File {filename} does not exist")
     except Exception as e:
         print("An error occured")
def main():
     while True:

         print("Welcome to the File Handling App")
         print("1. create File")
         print("2. View File")
         print("3. Delete File")
         print("4. read File")
         print("5. Edit File")
         print("6. Exit")
         choice = int(input("Enter your choice(1-6) : "))

         if choice == 1:
             filename = input("Enter file name to create : ")
             create_file(filename)
         elif choice == 2:
              view_file()

         elif choice == 3:
             filename = input("Enter file name to delete : ")
             delete_file(filename)
         elif choice == 4:
             filename = input("Enter file name to read : ")
             read_file(filename)
         elif choice == 5:
             filename = input("Enter file name to edit : ")
             edit_file(filename)
         elif choice == 6:
             print("Thank you for using this application")
             break
         else:
             print("Please enter a valid choice")

if __name__ == "__main__":
     main()

