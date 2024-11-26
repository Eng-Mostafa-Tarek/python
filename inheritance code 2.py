class person:
    def __init__(self, name, salary, car):
        self.name = name
        self.salary = salary
        self.car = car


class Mostafa(person):
    def __init__(self, name, salary, car, age):
        super().__init__(name, salary, car)
        self.age = age


obj1 = person("ali", 3000, "kia")

obj2 = Mostafa("omar", 5000, "BMW", "40")

print(obj1.name, obj1.salary, obj1.car)
print(obj2.name, obj2.salary, obj2.car, obj2.age)
