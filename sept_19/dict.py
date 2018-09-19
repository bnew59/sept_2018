
#first_name = input("Enter First Name: ")
#last_name = input("Enter Last Name: ")
#street = input("Enter Street: ")
#city = input("Enter City: ")
#state = input("Enter State: ")

#user = {"FirstName": first_name, "LastName": last_name}
#address = {"Street": street, "City" : city, "State" : state}

#user["Address"] = address

airports = {"IAH":"Intercontinental Aiport", "SEATEC": "Seattle Airport"}

#print(airports["SJO"])

# iterate through the dictionary by using a loop

for key in airports:
    print(airports[key])

#for some_key in dictionary:
    #dictionary[some_key]


dictionary = {"SomeKey":"SomeValue"}

print(dictionary["SomeKey"]) # prints out SomeValue

# dictionary with another dictionary as a value

#address = {"Street":"1200 Richmond Ave", "City" : "Houston"}
#address["Geo"] = {"Latitude":23.4, "Longitude": -101.34}

#user = { "FirstName" : "John", "LastName" : "Doe", "Address" :address }

# another way to add address to user
#user = { "FirstName" : "John", "LastName" : "Doe"}
#user["Address"] = address

# access city from the user
#user_address = user["Address"]
#print(user_address["City"])



#print(user)

#print(user["FirstName"])
#print(user["LastName"])
#print(user["Address"])
