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


print()

#Azam's code / notes from class

shopping_lists = []

class GroceryItem:
    def __init__(self,name,price,quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def updatePrice(self,new_price):
        self.price = new_price

    def __repr__(self):
        return f"Name = {self.name}, Price = {self.price}, Quantity = {self.quantity}"

another_grocery_item = GroceryItem("cookies",10,23)
another_grocery_item.updatePrice(100)
print(another_grocery_item.price)




class ShoppingList:
    def __init__(self,name):
        self.name = name
        self.address = ""
        self.store_number = ""
        self.shopping_list_card_number = ""
        self.items = []

# ask for shopping list
while True:

    shopping_list_name = input("Enter Shopping List Name or q to quit: ")
    shopping_list_address = input("Enter Shopping List Address ")
    shopping_list_store_number = input("Enter Shopping List Store Number ")

    if(shopping_list_name == "q"):
        break

    shopping_list = ShoppingList(shopping_list_name)
    shopping_list.address = shopping_list_address
    shopping_list.store_number = shopping_list_store_number

    # insert shopping list into the array
    #shopping_list_as_string = "{0} {1} {2}".format(shopping_list.name,shopping.address,shopping_list.store_number)

    shopping_lists.append(shopping_list)

    shopping_list.name = "Albertsons"

    # ask for grocery item
    while True:

        # ask for grocery items
        grocery_item_name = input("Enter Item Name: ")

        if(grocery_item_name == "q"):
            break

        # create a grocery item object
        grocery_item = GroceryItem(grocery_item_name,10)
        print(grocery_item)
        shopping_list.items.append(grocery_item)


#print(shopping_lists)
#print(len(shopping_lists))


class ShoppintList:
    def __init__(self, name):
        self.name = name
        self.address = "" #This creates an open string.

While True:

shopping_list_name = input ("Enter store name or q"):
if(shopping_list_name == "q"):
    break

shopping_list = ShoppingList(shopping_list_name)

#Put into the array
shopping_lists.append(shopping_list)






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