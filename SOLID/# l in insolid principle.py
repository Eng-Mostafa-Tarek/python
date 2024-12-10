class Bird:
    """
    Base class for birds. Subclasses may define additional behaviors.
    """

    def make_sound(self):
        print("Bird sound!")


class FlyingBird(Bird):
    def fly(self):
        print("Flying")


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")


class Ostrich(Bird):
    def run(self):
        print("Ostrich is running")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


sparrow = Sparrow()
ostrich = Ostrich()

make_bird_fly(sparrow)  # This works fine.
