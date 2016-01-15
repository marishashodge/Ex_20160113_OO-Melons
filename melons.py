"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
 
    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        

    def get_total(self):
        """Calculate price."""
        
        base_price = 5

        if "christmas" in self.species:
            base_price = base_price * 1.5
    
        total = (1 + self.tax) * self.qty * base_price
    
        if self.country_code != None and self.qty < 10:
            total = total + 3
        else:
            return total
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A tax free order that needs an inspection"""
    tax = 0.0

    passed_inspection = False

    def inspect_melons(self, passed):
        """Takes boolean determining if everything passed inspection"""


        if passed == True:
            self.passed_inspection = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
       
    order_type = "international"
    tax = 0.17
    
    def get_country_code(self):
        """Return the country code."""
        return self.country_code
