class Contract(object):
    
    def total_value(self):
        
        try:
            final_price = self.vehicle.sale_price() +(self.vehicle.interest * self.monthly_payments * self.vehicle.sale_price()/100)
        except:
            final_price = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_mulitiplier/self.length_in_months)
        return final_price - (final_price * self.discount)
        
    def monthly_value(self):
        try:
            monthly = self.monthly_payments
        except:
            monthly = self.length_in_months
        return self.total_value()/ monthly

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        self.discount = 0
        
        if self.customer.is_employee():
            self.discount = .1


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        self.discount = 0
        
        if self.customer.is_employee():
            self.discount = .1