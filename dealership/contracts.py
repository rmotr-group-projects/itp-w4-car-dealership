from .vehicles import Car, Truck, Motorcycle


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        
        if self.customer.is_employee():
            discount = 0.1
        else: 
            discount = 0

        buy_value = self.vehicle.sale_price() + (self.vehicle.INTEREST * self.monthly_payments * self.vehicle.sale_price() / 100) 
        return buy_value - (discount * buy_value)

    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        
        if self.customer.is_employee():
            discount = 0.1
        else: 
            discount = 0
        
        return (self.vehicle.sale_price() + (self.vehicle.sale_price()  * self.vehicle.LEASE_MULTI / self.length_in_months)) * ( 1 - discount )


    def monthly_value(self):
        return self.total_value() / self.length_in_months

