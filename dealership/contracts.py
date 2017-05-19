from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self,vehicle,customer):
        self.vehicle = vehicle
        self.customer = customer
        #self.vehicle.__class__.__name__
        if self.vehicle.__class__.__name__ == "Car":
            self.interest = 1.07
            self.multiplier = 1.2
        elif self.vehicle.__class__.__name__ == "Truck":
            self.interest = 1.11
            self.multiplier = 1.7
        elif self.vehicle.__class__.__name__ == "Motorcycle":
            self.interest = 1.03
            self.multiplier = 1
        #if self.customer.is_employee is True:
        if self.customer.is_employee():
            self.discount_rate = .9
        else:
            self.discount_rate = 1
            
            
# going to try something

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        return (self.vehicle.sale_price() + (self.interest * self.monthly_payments * self.vehicle.sale_price() / 100 )) * self.discount_rate
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self): 
        return (self.vehicle.sale_price() + (self.vehicle.sale_price() * self.multiplier / self.length_in_months)) * self.discount_rate
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months

