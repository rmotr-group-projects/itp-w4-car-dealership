class Contract(object):
    def __init__(self, customer, vehicle): 
        self.customer = customer 
        self.vehicle = vehicle 

    def total_value(self):
        pass
    
    def monthly_value(self):
        pass 

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        pass


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass
