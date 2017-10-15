# from dealership.vehicles import Vehicle as veh
# from dealership.customers import Person

class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments):
        super(Contract, self).__init__()
        self.monthly_payments = monthly_payments

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer, monthly_payments)
        
    def total_value(self):
        return self.sale_price() + (self.interest_rate() * self.monthly_payments * self.sale_price() / 100) #- (discount if employee)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months