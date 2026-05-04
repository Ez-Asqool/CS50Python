#Task Manager App
import sys


def main():
    hello()
    tasks = []
    while True:
        display_menu()
        action = get_action_number()
        match action:
            case "1":
                add_task(tasks)
            case "2":
                view_all_tasks(tasks)
            case "3":
                view_completed_tasks(tasks)
            case "4":
                view_pending_tasks(tasks)
            case "5":
                mark_task_completed(tasks)
            case "6":
                delete_task(tasks)
            case "7":
                sys.exit("Have a nice work, Good-bye")


def hello():
    print("Welcome in Task Manager App.")

def display_menu():
    print("1. Add Task \n2. View All Tasks \n3. View Completed Tasks"
        + "\n4. View Pending Tasks \n5. Mark Task as Completed \n6. Delete Task \n7. Exit")

def get_action_number():
    while True:
        action = input("Choose action number: ")
        match action:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                return action
            case _:
                print("Please, enter a valid action number.")


def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append({
        "task": task,
        "status": "pending"
    })
    print("Task Added Successfully.")

def view_all_tasks(tasks):
    if len(tasks) == 0:
        print("There is no tasks added to show it.!")
    else:
        for i in range(len(tasks)):
            print(f"Task [{i+1}]: {tasks[i]['task']}, Status: {tasks[i]['status']}")
        

def view_completed_tasks(tasks):
    if len(tasks) == 0:
        print("There is no tasks added to show it.!")
    else:
        anyCompletedTask = False
        for i in range(len(tasks)):
            if tasks[i]["status"] == "completed":
                print(f"Task [{i+1}]: {tasks[i]['task']}, Status: {tasks[i]['status']}")
                anyCompletedTask = True
            
        if not anyCompletedTask:
            print("There is no tasks marked as completed to show it.!")

def view_pending_tasks(tasks):
    if len(tasks) == 0:
        print("There is no tasks added to show it.!")
    else:
        anyPendingTask = False
        for i in range(len(tasks)):
            if tasks[i]["status"] == "pending":
                print(f"Task [{i+1}]: {tasks[i]['task']}, Status: {tasks[i]['status']}")
                anyPendingTask = True
            
        if not anyPendingTask:
            print("There is no tasks marked as pending to show it, All tasks completed.!")

def mark_task_completed(tasks):
    if len(tasks) == 0:
        print("There is no tasks added to choose from it.!")
    else:
        while True:
            view_all_tasks(tasks)
            try:
                taskNumber = int(input("Enter task number: "))
            except ValueError:
                print("Just (Integer-Positive) numbers is allowed.")
            else:
                if 0 < taskNumber <= len(tasks):
                    tasks[taskNumber-1]["status"] = "completed"
                    print(f"Task ({tasks[taskNumber-1]['task']}) Completed Successfully.")
                    break
                else:
                    print("Invalid task number.! Enter exists task number.")


def delete_task(tasks):
    if len(tasks) == 0:
        print("There is no tasks added to choose from it.!")
    else:
        while True:
            view_all_tasks(tasks)
            try:
                taskNumber = int(input("Enter task number: "))
            except ValueError:
                print("Just (Integer-Positive) numbers is allowed.")
            else:
                if 0 < taskNumber <= len(tasks):
                    task = tasks[taskNumber-1]
                    tasks.pop(taskNumber-1)
                    print(f"Task ({task['task']}) Removed Successfully.")
                    break
                else:
                    print("Invalid task number.! Enter exists task number.")



main()