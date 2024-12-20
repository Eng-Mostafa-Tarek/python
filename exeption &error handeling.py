x = 3
try:
    print(x / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
try:
    print(name + age)
except TypeError:
    print("TypeError: Cannot add two different data types")
except NameError:
    print("NameError")
except:
    print("handling any exception Error")


def A(a, b):
    try:
        c = (a + b) / (a - b)
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print(c)


A(2.0, 3.0)
A(3.0, 3.0)
