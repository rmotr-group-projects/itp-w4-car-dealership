from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    
        
    def total_value(self):
        if self.customer.is_employee() != True:
            return self.instance_total_value() 
        else:
            return self.instance_total_value()*0.9
    
    def monthly_value(self):
        if isinstance(self, BuyContract):
            return (self.total_value() / self.monthly_payments)
        elif isinstance(self, LeaseContract):
            return (self.total_value()/self.length_in_months)

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.monthly_payments = monthly_payments
        self.vehicle = vehicle
        self.customer = customer
        
    def get_interest_rate(self):
        if isinstance(self.vehicle, Car):
            return 1.07
        elif isinstance(self.vehicle, Motorcycle):
            return 1.03
        elif isinstance(self.vehicle, Truck):
            return 1.11
        
    
    def instance_total_value(self):
        total_value = self.vehicle.sale_price() + (self.get_interest_rate() * self.monthly_payments * self.vehicle.sale_price() / 100)
        return total_value

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.length_in_months = length_in_months
        self.vehicle = vehicle
        self.customer = customer
        
    def factor(self):
        if isinstance(self.vehicle, Car):
            return 1.2
        elif isinstance(self.vehicle, Motorcycle):
            return 1.0
        elif isinstance(self.vehicle, Truck):
            return 1.7
        
    
    def instance_total_value(self):
        return (self.vehicle.sale_price() + (self.factor() * self.vehicle.sale_price() / self.length_in_months))
        
        
        
        
        