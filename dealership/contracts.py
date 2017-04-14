from dealership.vehicles import Vehicle, Car, Truck, Motorcycle
from dealership.customers import Person, Employee, Customer

class Contract(object):
    
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        pass
    
    def monthly_value(self):
        pass



class BuyContract(Contract):
    def __init__(self, *args, **kwargs):
        Contract.__init__(self, *args, **kwargs)
        self.interest = 0
        if isinstance(self.vehicle, Car):
            self.interest = 1.07
        elif isinstance(self.vehicle, Motorcycle):
            self.interest = 1.03
        elif isinstance(self.vehicle, Truck):
            self.interest = 1.11
        else:
            self.interest = "What are you even driving"

 
    def total_value(self):
        total = float(self.vehicle.sale_price() + (self.interest * self.monthly_payments * self.vehicle.sale_price() / 100))
        if isinstance(self.customer, Employee):
            return total * 0.9
        else:
            return total 
        
    def monthly_value(self):
        return float(self.total_value() / self.monthly_payments)
    


class LeaseContract(Contract):
    
    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, vehicle, customer, length_in_months)
        self.length_in_months = length_in_months
    
    def total_value(self):
        lease_multiplier = 0
        if isinstance(self.vehicle, Car):
            lease_multiplier = self.vehicle.sale_price() * 1.2 / self.length_in_months
        elif isinstance(self.vehicle, Truck):
            lease_multiplier = self.vehicle.sale_price() * 1.7 / self.length_in_months
        elif isinstance(self.vehicle, Motorcycle):
            lease_multiplier = self.vehicle.sale_price() / self.length_in_months
        
        total = self.vehicle.sale_price() + lease_multiplier
        
        if isinstance(self.customer, Employee):
            return total * 0.9
        else:
            return total

    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
