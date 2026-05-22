class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Name :", self.name)
        print(self.name, "Marks :", self.marks)


# s1 = Student('BVNS', 100)
# s1.display()


class Employee:
    def __init__(self, ename, esal):
        self.ename = ename
        self.esal = esal

    def yearly_sal(self):
        ys = 12 * self.esal
        print(f"Yearly salary of employee : '{self.ename}' is : {ys}")

# e1 = Employee("PB", 50000)
# e1.yearly_sal()



class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def find_area(self):
        print(f"The area of the rectangle is {self.length} X {self.breadth} = {self.length * self.breadth}")

    def find_perimeter(self):
        peri = 2 * self.length * self.breadth
        print("The perimeter of the rectangle is :", peri)

# re = Rectangle(7,3)
# re.find_area()
# re.find_perimeter()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = 3.14 * self.radius * self.radius
        print("The area of the circle is :", a)

    def circumference(self):
        c = 2 * 3.14 * self.radius
        print("The circumference of circle is :", c)


# c = Circle(4)
# c.area()
# c.circumference()


class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
    
    def deposit(self, amt):
        self.balance += amt
        print("Amount deposited successfully")

    def withdraw(self, amt):
        if (self.balance - amt) < 0:
            print("Insufficient Balance")
        else:
            self.balance -= amt

    def check_balance(self):
        print("Account Holder :", self.acc_holder)
        print("Balance :", self.balance)


ba = BankAccount("Happy", 10000)
ba.check_balance()
ba.deposit(1200)
ba.check_balance()
ba.withdraw(300)
ba.check_balance()
ba.withdraw(1000)
ba.check_balance()