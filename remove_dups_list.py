
# Python code to remove duplicate elements 

def Remove(list):  # Remove is the name of the function, list is the variable or argument. all the numbers in
                    #duplicate below are loaded into list
    filtered_list = [] # filtered_list is a variable that is created and has an empty list initially, then is filled in by the
                    #comparison below of whether the number is in the list or not.
    for num in list: #this is a for loop that looks at each number in the argument called list above. num is a variable 
                    #that is used in the following lines. in list is getting each number in the list below.  
        if num not in filtered_list: #This if statement checks whether the number is in the filtered_list variable above
            filtered_list.append(num) # if it is not in the filtered_list variable it puts it in there
    return filtered_list # returns the completed filtered_list with all of the final integers / numbers in it. it return
                            # the value or numbers to the Remove in print.
      
# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
second_list = [1,2,1,2,2,3,4,1,10]

print(Remove(duplicate)) 
print(Remove(second_list))