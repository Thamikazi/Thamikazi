import os
print("Current Working Directory:", os.getcwd())

#=====importing libraries===========

import datetime

def read_users():
    """
    Reads and loads users from user.txt into a dictionary.
    Returns a dictionary whwre keys are usernames and values are passwords.
    """
    users = {}
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    username, password = parts
                    users[username] = password
                else:
                    print(f"Skipping invalid line in user.txt: {line.strip()}")
    return users

def read_tasks():
    """
    Reads and loads tasks from tasks.txt into a list od dictionaries.
    Each task is stored as a dictionary.
    """
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split(", ")
                task = {
                    "username": task_info[0],
                    "title": task_info[1],
                    "description": task_info[2],
                    "assigned_date": task_info[3],
                    "due_date": task_info[4],
                    "completed": task_info[5]
                }
                tasks.append(task)
    return tasks

def append_user(username, password):
    """
    Appends a nw user (username and password) to user.txt file
    """
    with open("user.txt", "a") as file:
        file.write(f"\n {username}, {password}\n")

def append_task(task):
    """
    Appends a new task (stored as a dictionary) to tasks.txt file
    """
    with open("tasks.txt", "a") as file:
        file.write(f"{task['username']}, {task['title']}, {task['description']}, {task['assigned_date']}, {task['due_date']}, {task['completed']}\n")

def display_menu(is_admin):
    """
    Displays the menu options based on the user's role.
    """
    print("Please select one of the following options:")
    if is_admin:
        print("r - Register a user")
        print("ds - Display statistics")
    print("a - Add a task")
    print("va - View all tasks")
    print("vm - View my tasks")
    print("e - Exit")

def register_user(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return
    
    password = input("Enter a new password: ")
    confirm_password = input("Confirm the password: ")
    if password == confirm_password:
        append_user(username, password)
        users.update(read_users())
        print("User registered successfully.")
    else:
        print("Passwords do not match. Please try again.")

def add_task():
    """
    Manages user registration.
    Prompts for a new username, checks for uniqueness, and adds user.
    """
    username = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    
    task = {
        "username": username,
        "title": title,
        "description": description,
        "assigned_date": datetime.date.today().strftime("%Y-%m-%d"),
        "due_date": due_date,
        "completed": "No"
    }
    append_task(task)
    print("Task added successfully.")

def view_all_tasks(tasks):

    """
    Displays all tasks in the tasks.txt file
    """
    task = read_tasks()

    for task in tasks:
        print(f"Username: {task['username']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Assigned Date: {task['assigned_date']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Completed: {task['completed']}")
        print("-" * 40)

def view_my_tasks(tasks, username):
    """
    Displays only the tasks of the logged in user
    """
    tasks = read_tasks()
    for task in tasks:
        if task['username'] == username:
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Assigned Date: {task['assigned_date']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: {task['completed']}")
            print("-" * 40)

def display_statistics(users, tasks):
    """
    Displays the total number of users and tasks.
    """
    print(f"Total number of users: {len(users)}")
    print(f"Total number of tasks: {len(tasks)}")

def main():
    """
    The main function that handles user login and menu interactions.
    """
    
    users = read_users()
    tasks = read_tasks()
               
    #====Login Section====
    logged_in = False

    while not logged_in:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and users[username] == password:
            logged_in = True
            is_admin = username == "admin"
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password. Please try again.")

    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    while True:
        display_menu(is_admin)
        choice = input("Enter your choice: ").lower()
        
        if choice == "r" and is_admin:
            register_user(users)
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks(tasks)
        elif choice == "vm":
            view_my_tasks(tasks, username)
        elif choice == "ds" and is_admin:
            display_statistics(users, tasks)
        elif choice == "e":
            print("Goodbye!")
            break
        else:
            print("Invalid choice or you don't have permission to perform this action. Please try again.")

if __name__ == "__main__":
    main()
