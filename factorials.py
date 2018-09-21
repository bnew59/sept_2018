#Assignment 1 - Write an app which asks users for the input and then prints the factorial for that number. 

# Python program to find the factorial of a number provided by the user.

# change the value for a different result

# uncomment to take input from the user


n=int(input("Input a number to compute the factiorial : "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))
#prints the factgorial of n



# check if the number is negative, positive or zero
#  print("Sorry, factorial does not exist for negative numbers")
#elif num == 0:
 #  print("The factorial of 0 is 1")
#else:
 #  for i in range(1,num + 1):
  #     factorial = factorial*i
   #print("The factorial of",num,"is",factorial)



#original copied code



# Python program to find the factorial of a number provided by the user.

# change the value for a different result
#num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

#factorial = 1

# check if the number is negative, positive or zero
#if num < 0:
#  print("Sorry, factorial does not exist for negative numbers")
#elif num == 0:
#   print("The factorial of 0 is 1")
#else:
 #  for i in range(1,num + 1):
  #     factorial = factorial*i
   #print("The factorial of",num,"is",factorial)

#number = int(input("Enter a number":))
#def factorial():
 #   (number % 2 == 0):
  #      print("Even")
   # else:
    #    print("odd")