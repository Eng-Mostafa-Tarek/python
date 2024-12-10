class Discount:
    """
    Base class for applying discounts. Subclasses should define their own discount logic.
    """

    def apply_discount(self, price):
        return price


class SeasonalDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9


class HolidayDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.8
