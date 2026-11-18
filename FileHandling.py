# File Management App

import os

def creat_file(filename):
     try:
      with  open(filename, "x") as f:
             print("File created")
     except FileExistsError:
         print("File already exists")
     except Exception as e:
         print("Error occured")
def view_file():
   try:
     files = os.listdir()
     if not files:
          print("No files found")
     else:
      print("Files in directory")
      for file in files:
          print(file)

   except FileNotFoundError:
        print("File does not exist")

def delete_file(filename):
      try:
         os.remove(filename)
         print("File deleted")
      except FileNotFoundError:
        print("File does not exist")

      except Exception as e:
          print("Error occured")



def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"File content: {content}")
    except FileNotFoundError:
        print("File does not exist")
    except Exception as e:
        print("Error occured")
def edit_file(filename):
    try:
        with open(filename, "a") as f:
             content = input("Enter new content: ")
             f.write(content + "\n")
             print("File edited")
    except FileNotFoundError:
           print("File does not exist")
    except Exception as e:
           print("Error occured")




def main():

   while True:

    print("Welcome to File Handling")

    print("1-create a new file")
    print("2-view existing file")
    print("3-delete existing file")
    print("4-read existing file")
    print("5-edit existing file")
    print("6-exit")
    choice = input("Enter your choice(1-6): ")
    if choice == '1':
        fielname = input("Enter file name: ")
        creat_file(fielname)
    elif choice == '2':
        view_file()
    elif choice == '3':
        filename = input("Enter file name to delete: ")
        delete_file(filename)
    elif choice == '4':
        filename=(input("Enter file name to read: "))
        read_file(filename)
    elif choice == '5':
        filename = input("Enter file name to edit: ")
        edit_file(filename)
    elif choice == '6':
        print("Thank you for using File Handling")
    else:
        print("Invalid input")
if __name__ == "__main__":
    main()





