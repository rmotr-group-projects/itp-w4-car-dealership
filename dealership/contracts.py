from .vehicles import Car, Motorcycle, Truck
from .customers import Customer, Employee

class Contract(object):
    def __init__(self,vehicle,customer):
        self.vehicle = vehicle
        self.customer = customer
        if isinstance(self.customer,Employee):
            self.DISCOUNTED_RATE = 0.9
        else:    
            self.DISCOUNTED_RATE = 1.0
        if isinstance(self.vehicle,Car):
            self.I = 1.07
            self.Multiplier = 1.2
            
        elif isinstance(self.vehicle,Motorcycle):
            self.I = 1.03
            self.Multiplier = 1.0
            
        elif isinstance(self.vehicle,Truck):
            self.I = 1.11
            self.Multiplier = 1.7
            
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract,self).__init__(vehicle,customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        return (self.vehicle.sale_price() + (self.I*self.monthly_payments*self.vehicle.sale_price()/100))*self.DISCOUNTED_RATE
        
    def monthly_value(self):
        return (self.total_value() / self.monthly_payments)
        
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract,self).__init__(vehicle,customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
        return (self.vehicle.sale_price() + (self.vehicle.sale_price()*self.Multiplier/self.length_in_months))*self.DISCOUNTED_RATE
        
    def monthly_value(self):
        return (self.total_value() / self.length_in_months)

