class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start():
        print("car started")

    def stop():
        print("stopped")



#Uses the features of Car

class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make.model)  # super initializes the super class which is class Car
        self.battery_life = 100  #adds to the super of Car
        # self.make = make   not needed since it is coming from the parent class
        # self.model = model

    def start(): #Uses this def for start, not the Car class start
        print("electric car started")

tesla = ElectricCar("Tesla", "Model x")
tesla.start()



class Animal:
    def __init__(self):
        pass
    def run(self):
        print("I run")

class Mamal(Animal):
    def __init__(self):
        super().__init__()

class Whale(Mamal)
    def __init__(self):
        super().__init__()

class Dog(Animal):
    def __init__(self):
        super().__init__()

class Cheetah(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print("I run very fast")





