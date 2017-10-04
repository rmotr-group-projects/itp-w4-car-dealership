class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__( vehicle, customer, monthly_payments)
        
    
    def total_value(self):
        total = self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price() / 100.00)
        total = total - self.customer.CUSTOMER_DISC * total
        return total

    def monthly_value(self):
        return self.total_value()/float(self.monthly_payments)
        
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__( vehicle, customer, length_in_months)
        self.monthly_payments = length_in_months
        
    def total_value(self):
        total = self.vehicle.sale_price() + (self.get_lease_multipler())
        total = total - self.customer.CUSTOMER_DISC * total
        return total

    def get_lease_multipler(self):
        return self.vehicle.sale_price() * self.vehicle.LEASE_MULTI / self.monthly_payments
        
    def monthly_value(self):
        return self.total_value()/float(self.monthly_payments)    