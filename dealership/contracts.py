class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        pass
    
    def total_value(self):
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price() / 100)) * .9
        else:
            return self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price() / 100) 
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        pass
    
    def total_value(self):
         if self.customer.is_employee():
           return (self.vehicle.sale_price() + ((self.vehicle.sale_price() * self.vehicle.M) / self.length_in_months)) *.9
         else:
           return (self.vehicle.sale_price() + ((self.vehicle.sale_price() * self.vehicle.M) / self.length_in_months))
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months