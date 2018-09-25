
#Assignment: Write a program which finds the smallest element in the array 




a=[1,2,3,4,6,7,99,88,999]
smallest = a[8]
for i in a:
    if i < smallest:
        smallest=i
print(smallest)