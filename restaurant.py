# Make a class called Restaurant. The __init__ method for Restaurant should store two attributes. 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restuarant() that prints a message indicating that the restaurant is open. 

# Make an instance called restaurant from your class. Print the two attributes individually, 
# and then call both methods.

restaurant_list = []

restaurant_input1 = input("Enter restaurant name: ")
restaurant_list.append(restaurant_input1)

restaurant_input2 = input("Enter restaurant cuisine: ")
restaurant_list.append(restaurant_input2)

class Restaurant:
    def __init__(self, restaurant_list):
        self.restaurant_list = restaurant_list
        

def describe_restaurant(self):
    print(Restaurant(restaurant_list)


# def displayColor(self):
#         print(f"The color is {self.color}")


#         def __init__(self, first_name, last_name, employee_id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.employee_id = employee_id
#         self.address = ""

# emp = Employee('John','Doe','EDRF456')

# class Car:
#     def __init__(self,make,model,color):
#         self.model = model
#         self.make = make
#         self.color = color

#     def changeColor(self,toColor):
#         print(f"Changing from {self.color} to {toColor}")
#         self.color = toColor
#         print("DONE Painting the car")

#     def openDoor(self):
#         # self.displayColor()
#         print("Open the door")

#     def displayColor(self):
#         print(f"The color is {self.color}")

# car = Car('Toyota','Camry','Orange')
# print(car.color)
# car.color = "Green"
# print(car.model)
# print(car.make)
# print(car.color)

# car.changeColor('Yellow')

# # object.methodname
# car.openDoor()

# car.displayColor()

# car2 = Car('Honda','Accord','grey')