from vehicles import *
from customers import *


class Contract(object):

    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def get_discount(self):
        if self.customer.is_employee():
            discount = .1
        else:
            discount = 0
        return discount


class BuyContract(Contract):

    interest = {
        'Car': 1.07,
        'Motorcycle': 1.03,
        'Truck': 1.11
     }

    def __init__(self, vehicle, customer, monthly_payments):
        Contract.__init__(self, vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        interest = BuyContract.interest[type(self.vehicle).__name__]
        sale_price = self.vehicle.sale_price()
        total = (sale_price + (interest * self.monthly_payments *
                 sale_price / 100))
        total = total - (total * self.get_discount())
        return total

    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):

    multiplier_value = {
        'Car': 1.2,
        'Motorcycle': 1,
        'Truck': 1.7
    }

    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        sale_price = self.vehicle.sale_price()
        vehicle_type = type(self.vehicle).__name__
        multiplier = (sale_price *
                      LeaseContract.multiplier_value[vehicle_type] /
                      self.length_in_months)
        total = sale_price + multiplier - self.get_discount()
        return total

    def monthly_value(self):
        return self.total_value() / self.length_in_months
