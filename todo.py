# Assignment 2 - TODO List
# You are responsible for creating a TODO list app. 
# Here are the requested features for the TODO list app: 
# - User should be able to add task by adding the title of the task 
# - User should be able to enter priority of the task 
# - User should be able to view all the tasks 
# - User should be able to remove the tasks 
# - User should be able to quit the app when "q" is pressed 
# HARD MODE: 
# - User should be able to sort the tasks based on priority 


# todo_list = []

# for i in range(0, 5): # set up loop to run 5 times
#     task = input("What is the task? ")
#         todo_list.append(task)
#     priority = input("What is the prioroty 1 to 10? ")
#         todo_list.append(priority)

# print(todo_list)


#Breakdown of what is needed to create the todo list
#1, take input from the user
#2 take priority from user
#3 Crete a task class

class Task:
    def __init__(self,title, priority):
        self.title = title
        self.priority = priority

#create an empty array
tasks = []

#Repeatedly ask for input with a while loop

while True:

    title = input("Enter task or q to quit")
    if(title == "q"):
        break
    priority = input("Enter priority")

    task = Task(title,priority)

 #add task items to tasks array above

    tasks.append(task)


for task in tasks:
    print(task.title)
    print(task.priority)

# print(task.title)
# print(task.priority)
