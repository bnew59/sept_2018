
#Assignment 2 - 

#Create an app which detects if the input word is a palindrome or not. 

 

#Palindromes are strings which when read from left to right are same as right to left. Examples below: 

#mom 

#dad 

#madam 

#The following strings are NOT palindrome: 

#cat != tac 

#car != rac 

#bus = sub 

# function which return reverse of a string 




def reverse(word): 
	return word[::-1] 

def isPalindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    else:
        return False


bug = input('Please input a word: ')

print(       isPalindrome(bug)        )


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








# print(factorial(n))
# Driver code 
# s = "malayalam"
# ans = isPalindrome(s) 

#if ans == 1: 
#	print("Yes") 
#else: 
#	print("No") 

