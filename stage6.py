#stage 6 - TO-DO list APP

import os
import json

TASK_FILE = "manage.json"

def load_task():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE) as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    return []


def save_task(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    save_task(tasks)
    print("Task added.")

def view_task(tasks):
    if not tasks:
        print("No tasks added.")
    status = "Done" if tasks["completed"] else "Not Done"
    for i, task in enumerate(tasks, 1):
        print(f"[{i}] {task['task']} [{status}]")

def mark_task(tasks):
    view_task(tasks)
    try:
        index = int(input("Enter task number to mark")) - 1
    except ValueError:
        print("Invalid input.")
        return
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked.")
        save_task(tasks)
    else:
        print("Task not found.")

def delete_task(tasks):
    view_task(tasks)
    try:
        index = int(input("Enter task number to delete")) - 1
    except ValueError:
        print("Invalid input.")
        return
    if 0 <=index <len(tasks):
        del tasks[index]
        print("Task deleted.")
        save_task(tasks)
    else:
        print("Task not found.")

def main():
    tasks = load_task()
    while True:
        print("----Welcome to TO-DO APP----")
        print("1. Add task")
        print("2. View task")
        print("3. Mark task")
        print("4. Delete task")
        print("5. Quit")
        try:
            choice = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            mark_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Thank you for using TO-DO APP.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

