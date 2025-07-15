"""student_info = {}

def add_student():
    name = input("Enter your name: ")
    subject = input("Enter your subject: ")
    try:
        grade = float(input("Enter your grade: "))
    except ValueError:
        print("Please enter a valid number for grade.")
        return

    record = {"subject": subject, "grade": grade}

    if name in student_info:
        student_info[name].append(record)
    else:
        student_info[name] = [record]

    print("Student added!")

def view_student():
    name = input("Enter student name to view: ")
    if name in student_info:
        records = student_info[name]
        print(f"\n{name} has {len(records)} record(s):")
        i = 1
        for record in records:
            print(f"\nRecord {i}")
            print("Subject:", record["subject"])
            print("Grade:", record["grade"])
            i += 1
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in student_info:
        records = student_info[name]
        if len(records) == 1:
            del student_info[name]
            print("Deleted the only record.")
        else:
            print(f"{name} has multiple records:")
            i = 1
            for record in records:
                print(f"{i}. Subject: {record['subject']}, Grade: {record['grade']}")
                i += 1
            try:
                choice = int(input("Enter the record number to delete: "))
                if 1 <= choice <= len(records):
                    del records[choice - 1]
                    print("Record deleted.")
                    if len(records) == 0:
                        del student_info[name]
                else:
                    print("Invalid record number.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Student not found.")

def list_all_students():
    if not student_info:
        print("No student records found.")
        return
    for name in student_info:
        print(f"\nStudent: {name}")
        records = student_info[name]
        i = 1
        for record in records:
            print(f"  Record {i}: Subject: {record['subject']}, Grade: {record['grade']}")
            i += 1

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Delete Student")
        print("4. List All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            list_all_students()
        elif choice == 5:
            print("Thank you for using this program.")
            break
        else:
            print("Invalid choice. Choose between 1 and 5.")

if __name__ == "__main__":
    main"""