import asyncio.tasks as tasks
from random import choice

tasks = []
print("____Welcome ToDoApp")

total_task = int(input("How many tasks would you like?"))
for i in range(1,total_task+1):
    task_name = input(f"Enter your task {i}: ")
    tasks.append(task_name)

print(f"today total task{tasks}")

while True:

    if choice == int(input(f"Enter task 1-add\n2-update\n3-delete\n4-view\n5-stop")):
        if choice == 1:
            add = input("Enter your task to add: ")
            tasks.append(add)
            print(f"adding task{tasks}")
        elif choice == 2:
            update = input("Enter your task to update: ")
            if update in tasks:
                 up = input("Enter your task to update: ")
                 ind = tasks.index(up)
                 tasks[ind] = up
                 print(f"updating task{up}")
        elif choice == 3:
         delete = input("Enter your task to delete: ")
         if delete in tasks:
                 ind = tasks.index(delete)
                 del tasks[ind]
                 print(f"deleting task{delete}")
        elif choice == 4:
            print(f"total task {tasks}")
        elif choice == 5:
            print("close program")
        else:
           print("invalid option")





