import json

tasks = []

def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        tasks = []
        print("No saved tasks found. Starting fresh!")
    except Exception as e:
        tasks = []
        print(f"Error loading tasks: {e}")

def show_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def mark_task_completed():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_no < len(tasks):
                tasks[task_no]["completed"] = True
                print(f"Task '{tasks[task_no]['task']}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_no < len(tasks):
                removed_task = tasks.pop(task_no)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
