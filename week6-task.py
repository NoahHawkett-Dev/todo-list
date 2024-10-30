'''
1. **Add a Task**: Users can add a new task with a description and a status (e.g., pending, completed).
2. **View Tasks**: Users can view all existing tasks along with their statuses.
3. **Update a Task**: Users can update the description or status of a task.
4. **Delete a Task**: Users can delete a task from the list.
5. **Persistent Storage**: The application should save tasks to a JSON file when changes are made and load them when the application starts.
'''
import os
import sys
import json
import time
from pystyle import Colors, Colorate, Center

os.system("title To-Do List")

printlogo = '''
  _______          _____          _      _     _   
 |__   __|        |  __ \        | |    (_)   | |  
    | | ___ ______| |  | | ___   | |     _ ___| |_ 
    | |/ _ \______| |  | |/ _ \  | |    | / __| __|
    | | (_) |     | |__| | (_) | | |____| \__ \ |_ 
    |_|\___/      |_____/ \___/  |______|_|___/\__|
    Noah Hawkett                                              
'''

logo = Center.XCenter(printlogo)

appdata = os.getenv("APPDATA")

data = "saveFile.json"
savePath = f"{appdata}\\todolist\\{data}"

red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"
white = "\033[1;37m"

def pathCheck():
    if not os.path.exists(f"{appdata}\\todolist"):
        os.makedirs(f"{appdata}\\todolist")

def loadTasks():
    pathCheck()
    if os.path.exists(savePath):
        with open(savePath, 'r') as file:
            return json.load(file)
    return []

def saveTasks(tasks):
    with open(savePath, 'w') as file:
        json.dump(tasks, file)

def printlogo():
   print(Colorate.Horizontal(Colors.blue_to_cyan, logo, 1))
   
def timeloop():
    while True:
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        yield currentTime

timegen = timeloop()

def getTime():
    return next(timegen)

now = getTime()

skipInput = False

def choice():
    while True:
        os.system("cls")
        printlogo()
        print(Center.XCenter(f"""
        {cyan}[ 1 ]{white} Add a task
        {cyan}[ 2 ]{white} View tasks
        {cyan}[ 3 ]{white} Update or delete a task
        {cyan}[ 4 ]{white} Exit
        """))
        
        print()
        appchoice = input(f"{cyan}[ >> ]{white} ")
        
        if appchoice == "1":
            addTask(tasks)
        elif appchoice == "2":
            os.system("cls")
            viewTasks(tasks)
        elif appchoice == "3":
            os.system("cls")
            updateDelete(tasks)
        elif appchoice == "4":
            sys.exit()
        else:
            print()
            input(f"{red}[ {now} ]{white} Invalid option, press ENTER to retry...")
            
def addTask(tasks):
    os.system("cls")
    printlogo()
    print()
    name = input(f"{cyan}[ >> ]{white} Enter task name: ")
    description = input(f"{cyan}[ >> ]{white} Enter task description: ")
    tasks.append({"name": name, "description": description, "status": "pending"})
    saveTasks(tasks)
    print(f"{green}[ {now} ]{white} Task added successfully!")
    input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")

def viewTasks(tasks):
    printlogo()
    print()
    if not tasks:
        print(f"{red}[ {now} ]{white} You have no tasks.")
    else:
        for i, task in enumerate(tasks):
            print(Center.XCenter(f"{cyan}[ {i + 1} ]{white} {task['name']} - {task['description']} - {task['status']}"))
    if not skipInput:
        print()
        input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")

def updateDelete(tasks):
    global skipInput
    os.system("cls")
    printlogo()
    print()
    if not tasks:
        print(f"{red}[ {now} ]{white} You have no tasks to update or delete.")
        input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")
        return
    print(Center.XCenter(f"{cyan}[ {now} ]{white} Enter task number to update/delete"))
    skipInput = True
    print()
    os.system("cls")
    viewTasks(tasks)
    print()
    skipInput = False
    task_num = input(f"{cyan}[ >> ]{white} ")

    if task_num.isdigit() and 0 < int(task_num) <= len(tasks):
        task_index = int(task_num) - 1
        print(Center.XCenter(f"{cyan}[ 1 ]{white} Update\n{cyan}[ 2 ]{white} Delete"))
        action = input(f"{cyan}[ >> ]{white} ")

        if action == '1':
            print(f"{cyan}[ {now} ]{white} Leave them blank to keep the same.")
            new_name = input(f"{cyan}[ >> ]{white} Enter new task name: ")
            if new_name == "":
                new_name = tasks[task_index]["name"]
            new_description = input(f"{cyan}[ >> ]{white} Enter new description: ")
            if new_description == "":
                new_description = tasks[task_index]["description"]
            new_status = input(f"{cyan}[ >> ]{white} Enter new status (pending/completed): ")
            if new_status == "":
                new_status = tasks[task_index]["status"]
            tasks[task_index]['name'] = new_name
            tasks[task_index]['description'] = new_description
            tasks[task_index]['status'] = new_status if new_status in ["pending", "completed"] else tasks[task_index]['status']
            saveTasks(tasks)
            print(f"{green}[ {now} ]{white} Task updated successfully!")
        elif action == '2':
            tasks.pop(task_index)
            saveTasks(tasks)
            print(f"{green}[ {now} ]{white} Task deleted successfully!")
        else:
            print(f"{red}[ {now} ]{white} Please choose a valid action.")
    else:
        print(f"{red}[ {now} ]{white} Please enter a valid task number.")
    input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")

if __name__ == "__main__":
    tasks = loadTasks()
    choice()