first_input = int(input("Enter A Number: "))

def fizz(a_num):
    if a_num % 5 ==0 and a_num % 3 ==0:
        return "FizzBuzz"
    if a_num % 3 == 0:
        return "Fizz" 
    if a_num % 5 == 0:
        return "Buzz"
    
output = fizz(first_input)
print(output)
