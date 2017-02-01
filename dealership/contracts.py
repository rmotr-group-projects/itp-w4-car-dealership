from vehicles import Vehicle
from customers import Person

class Contract(object):

    def employee_discount(self):
        return .9 if self.customer.is_employee() else 1.0
  
  
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        price = ((self.vehicle.sale_price() 
        + (self.vehicle.interest_rate * self.monthly_payments 
        * self.vehicle.sale_price() / 100 ))
        * self.employee_discount())
        return price
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
            

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        price = (self.vehicle.sale_price() 
        + (self.vehicle.sale_price() 
        * (self.vehicle.lease_rate / self.length_in_months)) 
        * self.employee_discount())
        return price 
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        
