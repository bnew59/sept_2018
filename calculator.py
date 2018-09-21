



def add(first_num, second_num):
    return first_num + second_num
    
def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

if operand == "+":
    result = add(first_num, second_num)

if operand == "-":
    result = subtract(first_num, second_num)

if operand == "*":
    result = multiply(first_num, second_num)

if operand == "/":
    result = divide(first_num, second_num)

first_num = int(input("Enter First Number: "))
operand = (input("Enter Operand: "))
second_num = int(input("Enter Second Number: "))

result = 0

print(result)


# Creates a message like
#Enter First NameB
#Enter Last NameN
#Enter CityH
#My name is B,N and I live in H


#def add(first_number, second_number):
#    return first_number + second_number

#def greet(name,age):
# print("Hello," + name)

#greet("John", 32)

#result = add(2,3)

#def display_car_info(make,model):
#   print("Make {0}, Model {1}")

#display_car_info(make = "Honda", model = "Accord")
