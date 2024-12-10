class Employee:
    """
    This is Single Responsibility Principle (SRP).
    It works as a separate class to make every class responsible for a single function.
    This improves performance and makes the code more flexible.
    """

    def __init__(self, name, role):
        self.name = name
        self.role = role


class SalaryCalculator:
    def calculate_salary(self, employee):
        pass


class Database:
    def save_to_database(self, employee):
        pass
