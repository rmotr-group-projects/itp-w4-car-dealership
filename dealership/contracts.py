from vehicles import *

class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.payment = monthly_payments

    def total_value(self):
        if self.vehicle == 'car':
            i = 1.07

        if self.vehicle == 'motorcycle':
            i = 1.03

        if self.vehicle == 'truck':
            i = 1.1

        if self.customer == 'customer':
            d = 1

        if self.customer == 'employee':
            d = 0.9

        return self.sale_price() + (i * self.monthly_payments * sale_price() / 100) * d

    def monthy_value():
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass

