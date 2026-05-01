# To Do List App
def main():
    print("Welcome in To-Do List App, ", end="")
    tasks = []
    while True:
        print("choose action number\n1. Add Task \n2. View Tasks \n3. Remove Task \n4. Exit ")
        action = get_action_number()
        match action:
            case "1":
                add_task(tasks)
            case "2":
                if len(tasks) == 0:
                    print("No tasks available.!!!")
                else:
                    view_tasks(tasks)
            case "3":
                if len(tasks) == 0:
                    print("No tasks available.!!!")
                else:
                    remove_task(tasks)
            case "4":
                print("Have a nice work, Good-bye")
                break




def get_action_number():
    while True:
        action = input("action number: ")
        match action:
            case "1" | "2" | "3" | "4":
                return action
            case _:
                print("Enter a valid action number")


def add_task(tasks):
    newTask = input("Enter new Task: ")
    tasks.append(newTask)
    print("New task added successfully.")

def view_tasks(tasks):
    for i in range(len(tasks)):
        print(f"Task {i+1} - {tasks[i]}")


def remove_task(tasks):
    while True:
        try:
            taskNumber = int(input("Enter task number to remove: "))
        except ValueError:
            print("Just integer numbers is allowed.")
        else:    
            if taskNumber <= 0 or taskNumber > len(tasks):
                print("Invalid task number, Enter exists task number.")
            else:
                removeTask = tasks[taskNumber-1]
                tasks.pop(taskNumber-1)
                print(f"Task({removeTask}) Removed Successfully")
                break


main()