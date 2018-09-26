# Assignment
# Grade: N/A
# View Grade Information. Opens a dialogue
# Assignment: 
# You are responsible for creating an app that manages groceries. Your groceries are characterized by 
# Shopping Lists which can contain grocery items. Here are the features you need to implement: 
# * You need to ask the user for the input. 
# - A user should be able to create a shopping list. A shopping list consists of a title and description. 
# Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc 
# - A user should be able to add multiple shoppings lists 
# - Give user an option to display the list 
# - A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title. Example Milk, Cookies, Paper, Napkins, Soda, Chips etc 

# Fiesta
# Milk, Soda, Fish 

# Walmart
# Paper, Napkins, Plate, Chips 

# Sams Club 
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey 

# class Task:
#     def __init__(self,title, priority):
#         self.title = title
#         self.priority = priority

#create an empty array
store = []

class Shopping_list:
    def __init__(self, store_name, location):
        self.store_name = store_name
        self.location = location
        self.id = len(store) + 1
        self.items = []
    
class Item:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity



    new_list = input("Enter Store: ")
    location = input("Enter Location: ")
    new_store = Shopping_list(new_list, location)
    store.append(new_store)

while True:

    answer = input("Add item to new list? Y/N: ").lower()
    if answer == 'y':
        item = input("Enter new item: ")
        quant = int(input("Enter quantity: "))
        new_item = Item(item, quant)
        new_store.items.append(new_item)
    if answer == 'n':
        break


#James' code






# class Task:
#     def __init__(self,title, priority):
#         self.title = title
#         self.priority = priority

# #create an empty array
# tasks = []

# #Repeatedly ask for input with a while loop

# while True:

#     title = input("Enter task or q to quit")
#     if(title == "q"):
#         break
#     priority = input("Enter priority")

#     task = Task(title,priority)

#  #add task items to tasks array above

#     tasks.append(task)


# for task in tasks:
#     print(task.title)
#     print(task.priority)