import json

def task_id():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            if tasks:
                return max(item["id_number"] for item in tasks) + 1
            return 1
    except Exception as e:
        return 1


def add_task(task):
    try:
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []
        tasks.append({"id_number": task_id(), "task": task, "status": "to do"})
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print("Error adding task:", e)

def list_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            print("\n")
            for task in tasks:
                print(f"{task['id_number']}. {task['task']} : {task['status']}")
            print("\n")
    except Exception as e:
        print("No tasks found.")
    
def update_task(id_num):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if task["id_number"] == id_num:
                    task["status"] = "done"
                    break
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print("Error updating task:", e)



option = 0

while option != "4":

    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Exit")

    option = input("select an option:")
    if option == "4":
        print("Exiting...")
        break

    if option == "1":
        while True:
            NewTask = input("enter you new task: ")
            add_task(NewTask)
            print("Task added successfully!")
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
            print(tasks)
            print("do you want to add another task? (yes/no)")
            response = input()
            if response.lower() != "yes":
                break
    if option == "2":
        list_tasks()
    if option == "3":
        update_id = int(input("Enter task ID to update: "))
        update_task(update_id)
        print(f"Task {update_id} was marked as done!")