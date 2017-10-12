class Contract(object):
    employee_discount = .1
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
        raise NotImplementedError()
    def monthly_value(self):
        raise NotImplementedError()
        
    def determine_final_price(self, undiscounted_value):
        if self.customer.is_employee():
            return undiscounted_value * (1 - self.__class__.employee_discount)
        else:
            return undiscounted_value
        

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    def total_value(self):
        undiscounted_value = self.vehicle.sale_price() + (self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price() / 100)
        return self.determine_final_price(undiscounted_value)
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):
        undiscounted_value = self.vehicle.sale_price() + self.lease_multiplier()
        return self.determine_final_price(undiscounted_value)
    def monthly_value(self):
        return self.total_value() / self.length_in_months
    def lease_multiplier(self):
        return self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER / self.length_in_months
        
        
        
    


