from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee

class Contract(object):
    
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
        raise NotImplementedError()
        
    def get_discount(self):
        self.discount = 0
        if self.customer.is_employee():
            self.discount = 0.1

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        
        if isinstance(self.vehicle, Car):
            interest = 1.07
        elif isinstance(self.vehicle, Truck):
            interest = 1.11
        elif isinstance(self.vehicle, Motorcycle):
            interest = 1.03
            
        total = self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100)
        return total - (self.discount * total)
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
            
        if isinstance(self.vehicle, Car):
            lease_multiplier = self.vehicle.sale_price() * 1.2 / self.length_in_months
        elif isinstance(self.vehicle, Truck):
            lease_multiplier = self.vehicle.sale_price() * 1.7 / self.length_in_months
        elif isinstance(self.vehicle, Motorcycle):
            lease_multiplier = self.vehicle.sale_price() * 1 / self.length_in_months
        
        total =  self.vehicle.sale_price() + lease_multiplier
        return total - (self.discount * total)
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months