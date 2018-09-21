# Assignment 3 - Exceptions

# Update your Calculator app to repeatedly ask the user to input the following:

# - Input first number

# - Input operand

# - Input second number

# If the operand is not "+" or +"-" or "*" or "/" then print a message to input correct operand.

# If the input is not a number than tell the user that they need to input numbers only.

# The user can quit the app by pressing "q" 

def add(first_num, second_num):
    return first_num + second_num
    
def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

result = 0

while True:


# while True:
#   try:
#       x = int(input("Please enter a number: "))
#       print('thank you!')
#       break
#   except ValueError:
#       print("Not a valid number, try again...")




    try:
        first_num = int(input("Enter First Number: "))
        operand = (input("Enter Operand: "))
        second_num = int(input("Enter Second Number: "))

        

    
        if operand == "+":
            result = add(first_num, second_num)

        elif operand == "-":
            result = subtract(first_num, second_num)

        elif operand == "*":
            result = multiply(first_num, second_num)

        elif operand == "/":
            result = divide(first_num, second_num)
        
        else:
            print("Invalid operand")

        print(result)

    except ValueError:
        print("Invalid Number")

    choice = input("Press q to quit - ")
    if choice == "q":
        break