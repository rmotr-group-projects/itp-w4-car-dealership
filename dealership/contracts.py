class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    
    def total_value(self):
        pass
    
    def monthly_value(self):
        pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract,self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        value = self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            value -= value * .1 #10% discout for employees
        return value
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        value = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.L / self.length_in_months)
        if self.customer.is_employee():
            value -= value * .1 #10% discout for employees
        return value
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months