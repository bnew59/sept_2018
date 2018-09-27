# Project - Pool Table Management
# Grade: N/A
# View Grade Information. Opens a dialogue
# You have just been hired by University of Houston as a developer. Your first task is to create 
# a pool table management app which will manage the pool tables in University Center Games Room. 

# Here are the requested features: 

# - As an admin you should be able to see all the tables (12) 

# - As an admin each table in the list should show, whether the table is OCCUPIED or NOT OCCUPIED. 

# - As an admin if the table is OCCUPIED then show the start time of the table, number of minutes played. 
# (Hardmode - If the minutes are > 60 then show them in terms of hours) 

# - As an admin you can only give out the tables that are NOT OCCUPIED. This means if pool table 8 is occupied and you 
# try to give it out then the app will print a message saying "Pool Table 8 is currently occupied". 

# - As an admin whenever I close the table it should write an entry in the text file / json file. 
# The file should be named in the following format: (11-22-2017.txt or 11-22-2017.json) 
# keeping track of all the tables. The entry can consists of the following information: 

# _________________________________________

# Pool Table Number 

# Start Date Time

# End Date Time 

# Total Time Played 

# Cost (if you are doing the hard mode) 

# ___________________________________________

 

# HARD MODE - Associate dollar amount for time played on the pool table. $30 per hour. 

# MORE HARD MODE - Write Unit Tests for your application

# EXTREMELY HARD MODE: Add the ability to email the final report (file) to an email address. 

# Posted Wed Sep 12, 2018 at 4:55 pm

import json
import datetime
import time

table1 = {"number": 1, "available": True}
table2 = {"number": 2, "available": True}
table3 = {"number": 3, "available": True}

table_data = [table1, table2, table3]

for table in table_data:
    
    if table["available"] == True:
        status = "Available"
    else:
        status = "Unavailable"
    print(str(table["number"] ) + " is " + status)



table_number = int(input("Enter table number: "))-1

selected_table = table_data[table_number]
print(selected_table)

while True:


    table_status = input("'u' for Unavailable, or 'A' for Available: ").lower()
    if table_status == "u":
        break
    if table_status == 'a':
        table_status = "Available"
        close_date = datetime.datetime.now().ctime()
        close_time = time.time()
        print(close_date)
    
    else:
        table_status = "Unavailable"
        open_date = datetime.datetime.now().ctime()
        open_time = time.time()
        total_time = round(open_time - close_time)
        cost = "$" + str(round(30/3600 * total_time,2))
        print(total_time, cost)

    





    
#         table_number.append({"Busy"}self.status)
# else 
#     file_object.write("Open"):
#         break



#     #     item = input("Enter new item: ")
#     #     quant = int(input("Enter quantity: "))
#     #     new_item = Item(item, quant)
#     #     new_store.items.append(new_item)
#     # if answer == 'n':
#     #     break



# with open("todo.txt","a") as file_object:
#     file_object.write(task_name)
#     file_object.write(task_priority)
#     # write an empty new line
#     # \n is the code for new line
#     file_object.write("\n")