
first_input = int(input("Enter A Number: "))

def even_odd(a_num):

    if a_num % 2 == 0:
        return "Even" 
    else:
        return "Odd" 
output = even_odd(first_input)
print(output)