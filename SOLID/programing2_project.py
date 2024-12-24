# SRP
class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# OCP
class Discount:
    def apply_discount(self, price):
        return price


class WeekendDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9


class LoyaltyDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.8


# LSP
class PaymentMethod:
    def pay(self, amount):
        print(amount)


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using cash.")


# ISP
class flying:
    def fly(self):
        pass


class swiming:
    def swim(self):
        pass


class Bird(flying):
    def fly(self):
        return "i can fly"


class fish(swiming):
    def swim(self):
        return "i can swim"


# DIP
class Engine:
    def start(self):
        print("Engine started.")


class ElectricEngine:
    def start(self):
        print("Electric engine started.")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is moving.")


# Testing SRP
room1 = Room(101, 150)
customer1 = Customer("Mostafa", "mostafa@gmail.com")
print(f"Room Number: {room1.room_number}, Price: {room1.price}")
print(f"Customer Name: {customer1.name}, Email: {customer1.email}")

# Testing OCP
price = 200
weekend_discount = WeekendDiscount()
loyalty_discount = LoyaltyDiscount()
print(f"Weekend Discounted Price: {weekend_discount.apply_discount(price)}")
print(f"Loyalty Discounted Price: {loyalty_discount.apply_discount(price)}")

# Testing LSP
payment1 = CreditCardPayment()
payment2 = CashPayment()
payment1.pay(500)
payment2.pay(300)

# Testing ISP
bird = Bird()
fish = fish()
print(bird.fly())
print(fish.swim())

# Testing DIP
petrol_engine = Engine()
electric_engine = ElectricEngine()
car1 = Car(petrol_engine)
car2 = Car(electric_engine)
car1.drive()
car2.drive()
