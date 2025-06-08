import json
import os

filename = "data.json"

dataDict = {"1": "Some task"}

def file_checker(file, defaultData):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        try:
            with open(file, "r") as f: 
                data = json.load(f)
        except json.JSONDecodeError:
            data = defaultData
            with open(file, "w") as f:
                json.dump(defaultData, f, indent=4)
    else:
        with open(file, "w") as f:
           json.dump(defaultData, f, indent=4)
        data = defaultData
    return data

def display_tasks():
    file = file_checker(filename, dataDict)
    for item_num, item_content in file.items(): 
        print(f"{item_num}: {item_content}\n")

def add_task():
    task = input("Add your task: ")
    count = len(dataDict)
    new_count = f"{count + 1}"
    dataDict[new_count] = task

    with open(filename, "w") as f:
        json.dump(dataDict, f, indent=4)
    print(f"✅ Task added as {new_count}")

def delete_task():
    file = file_checker(filename, dataDict)
    task_number = input("Add task number: ")

    if task_number in file:
        removed_task = file.pop(task_number)
        print(f"Task number{removed_task}!")
    with open(filename, "w") as f:
        json.dump(file, f, indent=4)
    


def main():
    while True:
        print("Choose action: \n 1. Show tasks\n 2. Add task \n 3. Delete task")
        choice = input("> ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()


main()
