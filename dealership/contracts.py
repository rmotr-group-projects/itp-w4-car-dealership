class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        
        self.monthly_payments = monthly_payments

    def total_value(self):  #total value of the contract to pay by a customer
        total_value = self.vehicle.sale_price() + ((self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price()) / 100)
        
        if self.customer.is_employee() is True:
            total_value = total_value * 0.9
            return total_value
        else:
            return total_value
    
    
    def monthly_value(self): # amount of money that a customer is supposed to pay monthly
        monthly_value = BuyContract.total_value(self) / self.monthly_payments
        return monthly_value


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        
        self.length_in_months = length_in_months

    def total_value(self):  
        lease_multiplier = (self.vehicle.sale_price() * self.vehicle.LEASE_MULT) / self.length_in_months
        total_value = self.vehicle.sale_price() + lease_multiplier 
        
        if self.customer.is_employee() is True:
            total_value = total_value * 0.9
            return total_value
        else:
            return total_value

    def monthly_value(self):
        monthly_value = LeaseContract.total_value(self) / self.length_in_months
        return monthly_value