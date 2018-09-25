


random_items = ["Alex",23,True,"Mary",12.34]
names = ["Alex","Mary","John","Steve","Kate","Paul","Bryan"]

# ask user for a name
input_name = input("Enter your name: ")

# add item to the end of names array
names.append(input_name)

# inserting item to an array at particular index
# names.insert(0,input_name)

#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])

# deleting an item from an array
del names[1]

#loop
# for loop

for index in range(0, len(names)):
    print(names[index])

# running loop in reverse order
#for index in range(len(names)-1,-1,-1):
#    print(names[index])
