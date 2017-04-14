from dealership.customers import *
from dealership.vehicles import *

class Contract(object):
    def total_value(self):
        buy_contract_rates = {Car : 1.07, Truck : 1.11, Motorcycle : 1.03}
        lease_contract_rates = {Car : 1.2, Truck : 1.7, Motorcycle : 1.0}
        discount = 1.0
        if isinstance(self.customer, Employee):
            discount = .9
                
# self.buy_contract_rates[self.vehicle.__class__]
                
        if isinstance(self, BuyContract): #checks to see if its a BuyContract or a LeaseContract
            return (self.vehicle.sale_price() + (buy_contract_rates[self.vehicle.__class__] * self.monthly_payments * self.vehicle.sale_price() / 100)) * discount
        
        else:    
            return (self.vehicle.sale_price() + ((self.vehicle.sale_price() * lease_contract_rates[self.vehicle.__class__] / self.length_in_months))) *  discount #This is the lease contract
            
            
        
    def monthly_value(self):
        if isinstance(self, BuyContract):
            return (self.total_value() / self.monthly_payments)
        return (self.total_value() / self.length_in_months)

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
   
        
