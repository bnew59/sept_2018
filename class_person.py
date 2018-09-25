class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print(other_person.name)
    
    def display(self):
        print(self.name)
        print(self.email)
        print(self.phone)

    def print_contact_info(self):
        print(str (self.email), (self.phone))

    def add_friends(self, new_friend):
        self.friends.append (new_friend)
        print(self.friends)

    def __repr__(self):
        return "name " + self.name 

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


# sonny.display()
# jordan.display()
# sonny.greet(jordan)
# jordan.greet(sonny)

# sonny.print_contact_info()
# jordan.print_contact_info()

jordan.add_friends(sonny)
sonny.add_friends(jordan)

#Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan
