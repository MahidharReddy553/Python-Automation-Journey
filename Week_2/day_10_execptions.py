def val_error():
    try:
        k = int(input("Enter integer input : "))
        print("the given input is :", k)
    except ValueError:
        print(f"The input must be an integer. Please enter an integer input value.")


def div_error():
    try:
        a = int(input("Enter value a: "))
        b = int(input("Enter value b: "))
        d = a / b
        print('The division of and "a" and "b" is :', d)
    except ZeroDivisionError:
        print('"b" value must not be zero')
    except ValueError:
        print("The inputs must be integer values")

def file_error():
    try:
        with open('Week_2/sample1.txt') as f:
            print(f)
    except FileNotFoundError:
        print("File not found. Please check it once or create it.")


def calculator():
    try:
        while True:
            try:
                print('1. Add\n' \
                '2. Divide\n' \
                '0. exit')

                c = int(input("Enter your choice (0/1/2) : "))

                if c == 1:
                    a = int(input("Enter value a: "))
                    b = int(input("Enter value b: "))
                    print('The addition of "a" and "b" is :', a + b)

                elif c == 2:
                    a = int(input("Enter value a: "))
                    b = int(input("Enter value b: "))
                    print("The division of 'a' and 'b' is :", a/b)

                elif c == 0:
                    break
                        
                else:
                    print("Please enter the valid choice. please enter (0/1/2)")

            except ValueError:
                print("The inputs must be integers, please enter the valid one.")
            except ZeroDivisionError:
                print("The 'b' value must not be zero.")
    finally:
        print("the calculator successfully terminated!!")

calculator()