
#while condition:
#    body of the while loop

#number = 0

#while number == 0:
#    print("Hello World")
#        break

def promptUserForInput():
    first_number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: "))
    return (first_number, second_number) # tuple

def add(a,b):
    return a+b

def display_result(no1,no2,choice,result):
    print("**********************")
    print("{0} {1} {2} = {3}".format(no1,choice,no2,result))
    #print(f"{no1} {choice} {no2} = {result}")
    print("**********************")

while True:

    result = 0
    choice = input("Enter your choice (+,-,*,\) or q to quit:")

    if(choice == "q"):
        break

    # promptUserForInput returns a tuple meaning two values
    (no1,no2) = promptUserForInput()

    if(choice == "+"):
        result = add(no1,no2)
    #elif(choice == "-"):
    #    result = subtract(no1,no2)

    #print("**********************")
    #print("{0} {1} {2} = {3}".format(no1,choice,no2,result))
    #print("**********************")

    display_result(no1,no2,choice,result)


print("Thank you for using calculator..")
