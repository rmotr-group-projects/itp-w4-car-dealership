class Contract(object):
    global discount
    discount = .10


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self, *args):
        obj_type = (type(self.vehicle).__name__)
        if obj_type == 'Car':
          interest = 1.07
        elif obj_type == 'Truck':
          interest = 1.11
        elif obj_type == 'Motorcycle':
          interest = 1.03
        
        total = self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100) 
        
        if self.customer.is_employee():
          return total - (total * discount)
        return total 
    
    def monthly_value(self):
      return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        obj_type = (type(self.vehicle).__name__)
        if obj_type == 'Car':
          lease_multiplier = 1.2
        elif obj_type == 'Truck':
          lease_multiplier = 1.7
        elif obj_type == 'Motorcycle':
          lease_multiplier = 1
        total = (self.vehicle.sale_price() + (self.vehicle.sale_price() * lease_multiplier / self.length_in_months)) 
    
        if self.customer.is_employee():
          return total - (total * discount)
        return total 
    
    def monthly_value(self):
      return self.total_value() / self.length_in_months
