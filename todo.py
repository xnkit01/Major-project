import json
import os

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

# Save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Add a task
def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category (Work, Personal, Urgent): ")
    
    task = Task(title, description, category)
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n--- Tasks ---")
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}. Title: {task.title}\n   Description: {task.description}\n   Category: {task.category}\n   Status: {status}\n")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1].mark_completed()
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to delete: "))
    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main program function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- Personal To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

# Start the to-do list application
if __name__ == "__main__":
    main()
