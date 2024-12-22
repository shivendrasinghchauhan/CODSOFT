
import json

# File to save and load tasks
FILE_PATH = "tasks.json"

# Load tasks from the file
def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file)

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

# Add a new task
def add_task(tasks):
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added!")

# Mark a task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as complete: ")) - 1
        tasks[task_num]["completed"] = True
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
        tasks.pop(task_num)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("Press 1, 2, 3, 4, 5")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
