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

# Employee System
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.dept)
        

m1 = Manager("bvns", 100000, "QA Testing")
m1.display_info()

## Bank Account

class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, d_amt):
        if d_amt < 0:
            print("Deposited amount should not be negative.")
        else:
            self.__balance += d_amt
            print("Deposited Amount:", d_amt)
            print("Amount deposited successfully...")
            # print(f"Balance:", self.__balance)

    def withdraw(self, w_amt):
        if w_amt < 0:
            print("Withdrawal amount should not be negative")
        else:
            if w_amt > self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance -= w_amt
                print("Withdrawal Amount:", w_amt)
                print("Amount withdrew successfully..")
                # print(f"Balance:", self.__balance)


    def check_balance(self):
        print("Account Holder Name:", self.name)
        print("Account Balance:", self.__balance)

b1 = BankAccount("PB", 200000)
# b1.check_balance()
b1.deposit(5000)
# b1.withdraw(9500)
b1.check_balance()