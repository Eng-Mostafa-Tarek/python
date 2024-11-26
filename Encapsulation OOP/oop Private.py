class Employee:
    def __init__(self, name, age, salary):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute
        self.__salary = salary  # Private attribute

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:  # Age validation
            self.__age = age
        else:
            raise ValueError("Age must be positive.")

    def set_salary(self, salary):
        if salary > 0:  # Salary validation
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive.")


# Example usage:
employee = Employee("Ahmed", 30, 15000)

# Access attributes using getter methods
print("Name:", employee.get_name())
print("Age:", employee.get_age())
print("Salary:", employee.get_salary())

# Modify attributes using setter methods
employee.set_name("Mostafa")
employee.set_age(29)
employee.set_salary(20000)

# Access updated attributes
print("\nUpdated Info:")
print("Name:", employee.get_name())
print("Age:", employee.get_age())
print("Salary:", employee.get_salary())
