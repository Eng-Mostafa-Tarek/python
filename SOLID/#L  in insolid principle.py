"""
            Liskov Substitution(LSP)
            Base class for birds. Subclasses may define additional behaviors.
"""


class Bird:
    pass


class flying(Bird):
    def fly(self):
        pass


class sparrow(flying):
    def fly(self):
        return "sparrow can fly"


class Ostrich(Bird):
    def run(self):
        return "ostrich can run"


obj = sparrow()
print(obj.fly())


obj2 = Ostrich()
print(obj2.run())
