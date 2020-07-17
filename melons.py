"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract SuperClass that other melons inherit from. """
    order_type = None   #assigned in sub-class
    tax = None          #assigned in sub-class

    def __init__(self, species, qty):
        """ Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'christmas melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the Government. """

    order_type = 'government'
    tax = 0

    def __init__(self, species, qty, passed_inspection):
        super().__init__(species, qty)
        self.passed_inspection = passed_inspection

    def mark_inspection(self, passed):
        self.passed_inspection = passed    


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = 'domestic'
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax and international fee."""
        total = super().get_total()

        # International fee for orders of less than 10
        if self.qty < 10:
            return total + 3    
        else:
            return total



    def get_country_code(self):
        """Return the country code."""

        return self.country_code


if __name__ == '__main__':
    order0 = InternationalMelonOrder('watermelon', 6, "AUS")
    order1 = DomesticMelonOrder('christmas melon', 5)
    order2 = GovernmentMelonOrder('watermelon', 50, False)
