"""
Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions.

"""


# Abstraction
class FlyingBehavior:
    def fly(self):
        pass


class WingedFlying(FlyingBehavior):
    def fly(self):
        print("Flying with wings")


class MotorFlying(FlyingBehavior):
    def fly(self):
        print("Flying with motors")


class Bird:
    def __init__(self, flying_behavior: FlyingBehavior):
        self.flying_behavior = flying_behavior

    def perform_fly(self):
        self.flying_behavior.fly()


sparrow = Bird(WingedFlying())
sparrow.perform_fly()
robot_bird = Bird(MotorFlying())
robot_bird.perform_fly()
