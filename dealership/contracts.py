from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        if self.customer.is_employee() == False:
            if isinstance(self.vehicle, Car) == True:
                return self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
            
            elif isinstance(self.vehicle, Motorcycle) == True:
                return self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
                
            elif isinstance(self.vehicle, Truck) == True:
                return self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
                
        else:
            if isinstance(self.vehicle, Car) == True:
                return (self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
            
            elif isinstance(self.vehicle, Motorcycle) == True:
                return (self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
                
            elif isinstance(self.vehicle, Truck) == True:
                return (self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
        
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        if isinstance(self.vehicle, Car) == True:
            return self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.2 / self.length_in_months)
        
        elif isinstance(self.vehicle, Motorcycle) == True:
            return self.vehicle.sale_price() + (self.vehicle.sale_price() * 1 / self.length_in_months)
            
        elif isinstance(self.vehicle, Truck) == True:
            return self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.7 / self.length_in_months)
            
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months