
class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        interest_rate = self.vehicle.INTEREST_RATE
        contract = self.vehicle.sale_price() + (interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)
        return (contract - contract * 0.1) if self.customer.is_employee() else contract 
    
    def monthly_value(self):
       return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def total_value(self):
        
        lease_multiplier = self.vehicle.lease_multiplier(self.length_in_months)
        
        lease_contract = self.vehicle.sale_price() + lease_multiplier
            
        return (lease_contract - lease_contract * 0.1) if self.customer.is_employee() else lease_contract
    
    def monthly_value(self):
       return self.total_value() / self.length_in_months
