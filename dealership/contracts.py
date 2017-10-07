from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee

class Contract(object):
    
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        self.discount = 0
        if self.customer.is_employee():
            self.discount = 0.1
        
    def total_value(self):
        raise NotImplementedError()
        
    def monthly_value(self):
        raise NotImplementedError()
        

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
            
        total = self.vehicle.sale_price() + (self.vehicle.INTEREST * self.monthly_payments * self.vehicle.sale_price() / 100)
        return total - (self.discount * total)
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
            
        lease_multiplier = self.vehicle.sale_price() * self.vehicle.SALE_MULTIPLIER / self.length_in_months
        
        total =  self.vehicle.sale_price() + lease_multiplier
        return total - (self.discount * total)
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months