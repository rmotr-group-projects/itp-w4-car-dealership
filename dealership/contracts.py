from vehicles import *
from customers import *


class Contract(object):
    def __init__(self):
        pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        if isinstance(self.vehicle, Car):
            interest_rate = 1.07
        elif isinstance(self.vehicle, Motorcycle):
            interest_rate = 1.03
        elif isinstance(self.vehicle, Truck):
            interest_rate = 1.11
        else:
            return "Invalid vehicle type"
        
        if isinstance(self.customer, Employee):
            #10% discount for employee
            discount = self.customer.discount_multiplyer * (self.vehicle.sale_price() + (interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100))
        elif isinstance(self.customer, Customer):
            discount = self.customer.discount_multiplyer * (self.vehicle.sale_price() + (interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100))
        else:
            return "Invalid customer type."
        
        return round((self.vehicle.sale_price() + (interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100) - discount), 2)
    
    def monthly_value(self):
        return round((self.total_value() / self.monthly_payments), 2)


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        #Lease Multiplyer
        if isinstance(self.vehicle, Car):
            lease_multiplyer = self.vehicle.sale_price() * 1.2 / self.length_in_months
        elif isinstance(self.vehicle, Motorcycle):
            lease_multiplyer = self.vehicle.sale_price() * 1 / self.length_in_months
        elif isinstance(self.vehicle, Truck):
            lease_multiplyer = self.vehicle.sale_price() * 1.7 / self.length_in_months
        else:
            return "Invalid vehicle type"
            
        if isinstance(self.customer, Employee):
            #10% discount for employee
            discount = self.customer.discount_multiplyer * (self.vehicle.sale_price() + lease_multiplyer)
        elif isinstance(self.customer, Customer):
            discount = self.customer.discount_multiplyer * (self.vehicle.sale_price() + lease_multiplyer)
        else:
            return "Invalid customer type."
            
        return round((self.vehicle.sale_price() + lease_multiplyer - discount), 2)
    
    def monthly_value(self):
        return round((self.total_value() / self.length_in_months), 2)
        
