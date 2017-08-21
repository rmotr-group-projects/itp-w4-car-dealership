#Customer can either buy or lease a car.
#Each class will have two methods: total_value(), monthly_value(). If employee, -10.0%

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
        if isinstance(self.vehicle, Car) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
        elif isinstance(self.vehicle, Car) and (not isinstance(self.customer, Employee)):
            return (self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 1.0

        elif isinstance(self.vehicle, Truck) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
        elif isinstance(self.vehicle, Truck) and (not isinstance(self.customer, Employee)):
            return (self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 1.0

        elif isinstance(self.vehicle, Motorcycle) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9
        else:
            return (self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 1.0
            
            
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


#total_value() = vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
#I = interest rate
#Car: 7% monthly (1.07 or 107%)
#Motorcycle: 3% monthly (1.03 or 103%)
#Truck: 11% monthly (1.11 or 111%)
#monthly_value = total_value() / monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    
    def total_value(self):
        if isinstance(self.vehicle, Car) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.2 / self.length_in_months)) * 0.9
        elif isinstance(self.vehicle, Car) and (not isinstance(self.customer, Employee)):
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.2 / self.length_in_months)) * 1.0
            
        elif isinstance(self.vehicle, Truck) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.7 / self.length_in_months)) * 0.9
        elif isinstance(self.vehicle, Truck) and (not isinstance(self.customer, Employee)):
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.7 / self.length_in_months)) * 1.0
            
        elif isinstance(self.vehicle, Motorcycle) and isinstance(self.customer, Employee):
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.0 / self.length_in_months)) * 0.9        
        else:
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.0 / self.length_in_months)) * 1.0          
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months



#total_value() = vehicle.sale_price() + (lease_multiplier) - (discount if employee) *
#lease multipler below:
#Car: sale_price() * 1.2 / length_in_months
#Motorcycle: sale_price() * 1 / length_in_months
#Truck: sale_price() * 1.7 / length_in_months
#monthly_value = total_value() / length_in_months
