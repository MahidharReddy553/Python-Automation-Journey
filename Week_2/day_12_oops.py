class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


    def display_info(self):
        print("Vehicle brand :", self.brand)
        print("Vehicle speed :", self.speed)


class Bike(Vehicle):
    def __init__(self, brand, speed, biketype):
        super().__init__(brand, speed)
        self.biketype = biketype

    def display(self):
        print("Bike Type :", self.biketype)

    
class Car(Vehicle):
    def __init__(self, brand, speed, biketype):
        super().__init__(brand, speed)
        self.fueltype = biketype

    def display(self):
        print("Car fuel Type :", self.fueltype)

# v1 = Vehicle('Volvo', '199kmph')
# v1.display_info()
# print('------------------------------')
# b1 = Bike('honda', '130kmph', 'Sports Bike')
# b1.display_info()
# b1.display()
# print('----------------------------')
# c1 = Car('Jeep', '199kmph', 'petrol')
# c1.display_info()
# c1.display()


class Animal:
    def __init__(self, species):
        self.species = species
    def get_species(self):
        return self.species
    
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def sound(self):
        print('Dog barks')

class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    def sound(self):
        print('Cat meows')    



d = Dog('Pug')
print('The dog species is :', d.get_species())
d.sound()

c = Cat('Siberian')
print("The cat species is :", c.get_species())
c.sound()
