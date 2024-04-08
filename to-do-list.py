tasks = []

def add_task(task):
    tasks.append(task)

def display_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
def delete_tasks(tasks):
    tasks.pop()
# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Updatr Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        print("Task added successfully!")
    elif choice == "2":
        print("\nTasks:")
        display_tasks()
    elif choice == "3":
        delete_tasks(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
