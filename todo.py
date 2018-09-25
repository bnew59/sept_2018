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


todo_list = []

for i in range(0, 5): # set up loop to run 5 times
	task = input("What is the task? ")
        todo_list.append(task)
    priority = input("What is the prioroty 1 to 10? ")
        todo_list.append(priority)

print(todo_list)
