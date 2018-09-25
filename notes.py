9/19

# Dictionaries


#first_name = input("Enter First Name: ")
#last_name = input("Enter Last Name: ")
#street = input("Enter Street: ")
#city = input("Enter City: ")
#state = input("Enter State: ")

#user = {"FirstName": first_name, "LastName": last_name}
#address = {"Street": street, "City" : city, "State" : state}

#user["Address"] = address

airports = {"IAH":"Intercontinental Aiport", "SEATEC": "Seattle Airport"}

#print(airports["SJO"])

# iterate through the dictionary by using a loop

for key in airports:
    print(airports[key])

#for some_key in dictionary:
    #dictionary[some_key]


dictionary = {"SomeKey":"SomeValue"}

print(dictionary["SomeKey"]) # prints out SomeValue

# dictionary with another dictionary as a value

#address = {"Street":"1200 Richmond Ave", "City" : "Houston"}
#address["Geo"] = {"Latitude":23.4, "Longitude": -101.34}

#user = { "FirstName" : "John", "LastName" : "Doe", "Address" :address }

# another way to add address to user
#user = { "FirstName" : "John", "LastName" : "Doe"}
#user["Address"] = address

# access city from the user
#user_address = user["Address"]
#print(user_address["City"])



#print(user)

#print(user["FirstName"])
#print(user["LastName"])
#print(user["Address"])





#Creating Arrays


name = "John"

random_items = ["Alex",23,True,"Mary",12.34]
names = ["Alex","Mary","John","Steve","Kate","Paul","Bryan"]

# ask user for a name
input_name = input("Enter your name: ")

# add item to the end of names array
names.append(input_name)

# inserting item to an array at particular index
# names.insert(0,input_name)

#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])

# deleting an item from an array
del names[1]

#loop
# for loop

for index in range(0, len(names),1):
    print(names[index])

# running loop in reverse order
#for index in range(len(names)-1,-1,-1):
#    print(names[index])









# is letter a vowel?

letter = input("Enter a letter")

def if_vowel():
    if (letter == "A", or letter == "E", or letter == "I").tolower
    #.tolower changes to lower case
        Result = True
    return Result
result = if_vowel()
print result


#even, odd numbers

number = int(input("Enter a number":))
def enevodd():
    if(number % 2 == 0):
        print("Even")
    else:
        print("odd")

Lists -
Lists are arrays - like lists of news items
see notebook for notes
Array example

name = "John"

RandomItems = ("Alex,23,True,Mary)

Names = ("John,"MAry","Steve")
#an array of Names
# to access Alex...
print([Names[0]])

#to print all members int he array you can print 0,1,2,3  or do a loop
#loop
# for loop is used when you know the start and end

#for index in range(starting_index, ending index) is the format
for index in range((0, 4) 
#or can use len for length of the index
for index in range(0,len(names)):
    print(names[index])

#always go one past the number by one because you start at 0

#to print in reverse order
for index in range(-1,-1,-1):
    print(names[index])

# add names by the user

random_items = ("Alex,23,True,Mary)

Names = ("John,"MAry","Steve")
input_name = input("Enter Name")
names.append(input_name)  #appends to the end of the list
for index in range(-1,-1,-1):
    print(names[index])

#to insert to an array - insert lets you state where to insert
names.insert(0,input_name)

#deleting an item from an array
del names[2] #deletes the third item in the array

#while loops
#while - some condition and then a value

while 1 == 1:
    print("Hello World")
#this is an infinite loop

while number == 0::
    print("Hello World")
    number = 1
#this would break the loop becuase number is changed to 1

while number == 0::
    print("Hello World")
    number = 0
        break
    #this also breaks the loop

#asking user for input in the transaction

choice = input("Enter your choice (+,-,<,*,/) or q to quit:)
first_number = input("Enter first number")
second_number = input("Enter second nuber")

if (choice == "+");
    print first_number + second_number)


#creating a infinity loop

while True:
    choice = input("Enter your choice (+,-,<,*,/) or q to quit:)
        if (choice == "q"):
        break
    first_number = input("Enter first number")
    second_number = input("Enter second nuber")

    if (choice == "+");
        print first_number + second_number)

print("Q entered")  #This is at the bottom because you have broken the loop by pressing q

#ways to make this code better

def PromptUserForInput():
    first_number = int(input("Enter first number"))
    second_number = int((input("Enter second nuber"))
    return (first_number, second_number)

while True:
    choice = input("Enter your choice (+,-,<,*,/) or q to quit:)
        if (choice == "q"):
        break

    (no1,no2) PromptUserForInput()

    if (choice == "+");
        result = add(no1 + no2)
    elif(choice == "-")

        print(result)

print("Q entered")
    


#Dictionaries - has Key and Value
#Keys are usually strings  Values can be anything, strings, arrays, integer, float, etc.

dictionary = {"SomeKey": "SomeValue"}
print(dictionary[SomeKey"] #prints SomeValue

#another dictionary for addresses
address = {"Street": "1200 Richmond", "City":"Houston"}
    print(user["address"])

#dict with another dict as a value

user = {"FirstName": "John", "LastName": "Doe", "Address": address}

#to access city from user
user_address = user["address"]
print(user_address["City"])

print(user["FirstName"]) #prints John

#Another dictionary for airports

airports = {"IAH": "Houston", "Seatac": "Seattle"}
print(airports[IAH])

#go through the dictionary using a loop

for key in airports:
    print(airports[key])


Python logic process


Checks if this is a Palindrome
def reverse(word): 
	return word[::-1] 

def isPalindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    else:
        return False


bug = input('Please input a word: ')

print(isPalindrome(bug))


# Logic:
# 1. The processor starts at the top and puts the 2 def functions in memory
# 2. Then it gets to bug and asks for a word like house
# 3. Next it goes to the print command which refers to the isPalindrome function
# 4. isPalindrome's (s) is a placeholder to accept whatever is passed into it which at this point is "house"
# 5. isPalindrome's function then does the reverse command of (s), or house which makes it "esuoh" and then the
# if statement checks if (s) from isPalindrome which is "house" is + to the variable of rev which is "esuoh"
# 6. If it is then it returns True, if not it returns False
#7. bug = input... is not calculated again becuase it was already input into once, so it breaks and does not loop 
#after that
#8. Then it goes to the print statement and prints False because it is printing the oucome of isPalindrome
#which is False in this case. The (bug) part of print was only used to define the input of house to pass it 
#to isPalindrome, or #3.



9/20  Notes

Loops and Errors were explained. The recording is on Schoology
Loop using while
while True:
  try:
      x = int(input("Please enter a number: "))
      print('thank you!')
      break
  except ValueError:
      print("Not a valid number, try again...")

# The try statement works as follows.
# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution 
# of the try statement is finished. If an exception occurs during execution of the try clause, 
# the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, 
# the except clause is executed, and then execution continues after the try statement.
# If an exception occurs which does not match the exception named in the except clause, 
# it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution 
# stops with a message as shown above.

# A try statement may have more than one except clause, to specify handlers for different exceptions. 
# At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, 
# not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, 
# for example: except (RuntimeError, TypeError, NameError):

9/21 notes

Import commands

import math # imports from the math folder
#what you are importing needs to be in the same directory (folder) that you are in



Tuples - lists that cannot be changed. brackets make it a tuple, brackets make it a list

thistuple = ('apple', 'banana', 'orange')

thislist = ['zucchini', 'pepper', 'broccoli']

#you can add, remove etc. from thislist.


List vs array

you can perform more math on an array



9/24 Notes

classes and objects - needed in all languages

class - a blueprint thst allows you to create other things
Blueprint - basic properties of something I am talking about
    has a surface
    material
    4 legs
    Cost
this could become any table

now Blueprint becomes Table

Car blueprint - the class name should always be singular
These are properties or attributes of the car
    make
    Model
    Color


how do we create a BMW from thgis?
    make = BMW
    model= 320
    color = white

using the Car blueprint oe class I created a BMW
create another class

the properties are,
    lastname
    firstname
    dateofbirth
    social

the class is Person


Actions - things the car can do
    start the car
    stop the car
    turn

create a class now for coding

class Car:
    def __init__(self): #this is an initializer or constructor. self is an object in the class car
        self.make = "BMW"  #These are the instances / objects of the "car" class
        self.model = "Series 3"
        self.year = "2018"
        print("initializing a car")
        print(self)

#creates an object / instance of Car class
car = Car("Honda", "Accord", "2018")

print(car.make)
print(car.model)
print(car.year)

#creating a Car class OBJECT called car
car = Car("Toyota", "camry", "2018") #This uses Car class to print out the toyota attributes
print(car.make)
print(car.model)
print(car.year)


#__init__ is a built in function
Another way is

class DirvingLicense
    def __init__(self, firstname, last,name)


    #create a class called user with forst and last name

    class User:
        def __init__(self, first_name, last_name)

user = User("Jphn", "doe")
print(user)

#Now add capability to have blamk areas to add to

#self is always the object on which the function is called
class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last+name
            self.street = ""
            self.state = ""
            self.addresses = []  # creates an array for multiple addresses


user = User("Jphn", "doe")

user.street = "2017 Rosewood"

print(user)




class Battery:
    def __init__(self, life, manufacturer):
        self.life = life
        self.manufacturer = manufacturer

class ElectricCar:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self. battery = Battery

    def print_funct(self):
        print("Make" = {0}, Model = {1}, Battery = {2})

battery = Battery(100, "CC")

car = ElectricCar("Tesla", "Model X", battery)

print



class Task:
    def __init__(self, title, priority):
        sefl.title = titleself.priority = priority

task = Task("Wash the car", High)

task2 = ...

tasks = [] # crete aqn array

