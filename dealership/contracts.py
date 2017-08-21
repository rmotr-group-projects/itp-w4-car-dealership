from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer


class BuyContract(Contract):
    
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        if isinstance(self.vehicle, Car):
            i = 1.07
        elif isinstance(self.vehicle, Motorcycle):
            i = 1.03
        elif isinstance(self.vehicle, Truck):
            i = 1.11
        if self.customer.is_employee():
            d = .9
        else:
            d = 1
        total_value = (self.vehicle.sale_price() + (i * self.monthly_payments * self.vehicle.sale_price() / 100)) * d
        return total_value

    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        if isinstance(self.vehicle, Car):
            i = 1.2
        elif isinstance(self.vehicle, Motorcycle):
            i = 1
        elif isinstance(self.vehicle, Truck):
            i = 1.7
        if self.customer.is_employee():
            d = .9
        else:
            d = 1
        total_value = (self.vehicle.sale_price() + (self.vehicle.sale_price() * i / self.length_in_months)) * d
        return total_value
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        
