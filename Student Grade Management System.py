from ImportMethod import student

student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade

    print("Student Added Successfully")
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print("Student Updated Successfully")
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print("Student Deleted Successfully")
def view_student(name):
    if  student_grades:
        print(student_grades[name])
        for name, grade in student_grades.items():
            print(f"{name}: viewed successfully {grade}")
def main():
    print("Student Grade Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Student")
    print("5. Exit")
    choice = input("Enter your choice(1-5): ")
    if choice == '1':
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        update_student(name, grade)
    elif choice == '3':
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        delete_student(name)

    elif choice == '4':
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        view_student()
    elif choice == '5':
        print("Thank you for using Student Grade Management System")
    else:
        print("Invalid input")
if __name__ == "__main__":
    main()