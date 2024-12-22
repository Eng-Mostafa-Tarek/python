from abc import ABC, abstractmethod

class FlyingAnimal(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmingAnimal(ABC):
    @abstractmethod
    def swim(self):
        pass

class RunningAnimal(ABC):
    @abstractmethod
    def run(self):
        pass

class Bird(FlyingAnimal, RunningAnimal):
    def fly(self):
        print("Bird is flying")

    def run(self):
        print("Bird is running")

class Fish(SwimmingAnimal):
    def swim(self):
        print("Fish is swimming")

class Dog(RunningAnimal, SwimmingAnimal):
    def run(self):
        print("Dog is running")

    def swim(self):
        print("Dog is swimming")


def make_fly(animal: FlyingAnimal):
    animal.fly()

def make_swim(animal: SwimmingAnimal):
    animal.swim()

bird = Bird()
fish = Fish()
dog = Dog()

make_fly(bird)   
make_swim(fish)
make_swim(dog) 
