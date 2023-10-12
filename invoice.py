#!/usr/bin/python3

class Invoice:
    """A simple invoice class"""

    def __init__(self, part_number, part_description, quantity, price):
        """Initializes an instance of an invoice"""
        self.__part_number = part_number
        self.__part_description = part_description
        self.__quantity = quantity
        self.__price = price

    @property
    def part_number(self):
        """getter for part_number"""
        return self.__part_number

    @part_number.setter
    def part_number(self, part_number):
        """setter for part_number"""
        self.__part_number = part_number

    @property
    def part_description(self):
        """getter for part_description"""
        return self.__part_description

    @part_description.setter
    def part_description(self, part_description):
        """Setter for part_description"""
        self.__part_description = part_description

    @property
    def quantity(self):
        """getter for quantity"""
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        """setter for part description"""
        self.__quantity = 0 if quantity < 0 else quantity

    @property
    def price(self):
        """Getter for price"""
        return self.__price

    @price.setter
    def price(self, price):
        """setter for price"""
        self.__price = 0.0 if price < 0 else price

    def get_invoice_amount(self):
        """Calculates the invoice amount"""
        return self.__quantity * self.__price

my_invoice = Invoice(56, "Nice part", 2, 35.2)
print(my_invoice.get_invoice_amount())
