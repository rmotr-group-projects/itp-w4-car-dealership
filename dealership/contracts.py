class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        val = self.vehicle.sale_price() + (self.monthly_payments * self.vehicle.INTEREST_RATE * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            return val - (val * .10)
        else:
            return val 
        
    def monthly_value(self):
        
        return self.total_value() / self.monthly_payments
        
    


class LeaseContract(Contract):
    
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def total_value(self):
        lease_val = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER / self.length_in_months)
        if self.customer.is_employee():
            return lease_val - (lease_val * .10)
        else:
            return lease_val
            
    def monthly_value(self):
        return self.total_value() / self.length_in_months

