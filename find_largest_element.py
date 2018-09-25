
#Assignment: Write a program which finds the largest element in the array 

# def largest_element(thing):
#     for num in thing:
#         if num + 1 in 


# elements = [1, 2, 3, 4]


a=[1,2,3,4,6,7,99,88,999]
max = a[0]
for i in a:
    if i > max:
        max=i
print(max)