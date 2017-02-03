from vehicles import *
from customers import *

class Contract(object):
    pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle=vehicle
        self.customer=customer
        self.monthly_payments=monthly_payments
    
    def total_value(self):
        interest=float(self.vehicle.get_interest_rate())
        if self.customer.is_employee() is True:
            discount=(self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100))*.1
        elif self.customer.is_employee() is False:
            discount=0
        return self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100)-discount

    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    def total_value(self):
        multiplier=self.vehicle.get_lease_multiplier(self.vehicle.sale_price, self.length_in_months)    
        if self.customer.is_employee() is True:
            discount=self.vehicle.sale_price() + (multiplier)*.1
            return self.vehicle.sale_price() + (multiplier)-discount
        elif self.customer.is_employee() is False:
            return self.vehicle.sale_price() +multiplier
    def monthly_value(self):
        return self.total_value() / self.length_in_months
