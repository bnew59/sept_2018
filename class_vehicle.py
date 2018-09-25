class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __repr__(self):
        return '%s, %s, %s' % (self.make,self.model,self.year)

f150 = Vehicle("Ford", "F150", "2015")
print(f150.make)
print(f150.model)
print(f150.year)

print(f150)