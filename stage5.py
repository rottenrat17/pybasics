#stage 5 -less go
#student management system

student_info = {}

def add_student():
    name = input("Enter your name: ")
    subject = input("Enter your subject: ")
    try:
        grade = float(input("Enter your grade: "))
    except ValueError:
        print("Please enter a number.")
        return

    student_info[name] = {
        "subject": subject,
        "grade": grade
    }
    print(f"Student added.")
    print(student_info)

def view_student():
    name = input("Enter student name to view: ")
    if name in student_info:
        info = student_info[name]
        print(f'Student namee = {name}')
        print(f'Student subject = {info["subject"]}')
        print(f'Student grade = {info["grade"]}')
    else:
        print("Student not found.")

def search_student():
    name = input("Enter student name to search: ")
    if name in student_info:
        info = student_info[name]
        print(f'Student name = {name}')
        print(f'Student subject = {info["subject"]}')
        print(f'Student grade = {info["grade"]}')
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in student_info:
        del student_info[name]
        print(f"Student name: {name} deleted.")
    else:
        print("Student not found.")


def list_all_student():
    if not student_info:
        print("No students found.")
        return
    print("\nAll Student Records: ")
    for name, info in student_info.items():
        print(f"Name: {name}")
        print(f"Subject: {info["subject"]}")
        print(f"Grade: {info["grade"]}")
        print("-" * 30)


def main():
    while True:
        print("Welcome to Student Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. List All Student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            list_all_student()
        elif choice == 6:
            print("Thank you for using this program")
            break
        else:
            print("Invalid choice. Choose again between 1 and 5.")

if __name__ == "__main__":
    main()