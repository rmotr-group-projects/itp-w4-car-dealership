class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    def total_value():  #total value of the contract to pay by a customer
        pass
    
    def monthly_value(): # amount of money that a customer is supposed to pay monthly
        pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        
        self.monthly_payments = monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        
        self.length_in_months = length_in_months
