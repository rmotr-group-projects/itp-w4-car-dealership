from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee

class Contract(object):
    
    def total_value(self):
        raise NotImplementedError()
    
    def monthly_value(self):
        raise NotImplementedError()
    
    
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

    def total_value(self):
        i_rate = None 
        
        if self.vehicle.__class__.__name__ == "Car":
            i_rate = 1.07
        elif self.vehicle.__class__.__name__ == "Motorcycle":
            i_rate = 1.03
        else:
            i_rate = 1.11
        
        t_price = self.vehicle.sale_price() + (i_rate * self.monthly_payments * self.vehicle.sale_price() / 100)
            
        if self.customer.__class__.__name__ == "Employee":
            return t_price * 0.9
        else:
            return t_price
    
    def monthly_value(self):
        monthly_value = BuyContract.total_value(self) / self.monthly_payments
        return monthly_value


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        lease_multiplier = None
        
        if self.vehicle.__class__.__name__ == "Car":
            lease_multiplier = 1.2
        elif self.vehicle.__class__.__name__ == "Motorcycle":
            lease_multiplier = 1
        else:
            lease_multiplier = 1.7
            
        t_price = (self.vehicle.sale_price()) + (self.vehicle.sale_price() * lease_multiplier) / (self.length_in_months)
        
        if self.customer.__class__.__name__ == "Customer":
            return t_price
        else:
            return t_price * 0.9


    def monthly_value(self):
        monthly_value = LeaseContract.total_value(self) / self.length_in_months
        return monthly_value
        
