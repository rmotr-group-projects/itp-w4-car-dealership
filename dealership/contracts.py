class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    def sale_price(self):
        sale_price = self.vehicle.sale_price()
        if self.customer.is_employee():
            sale_price = sale_price*0.9
        return sale_price

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        return self.sale_price() + (self.vehicle.INTEREST_RATE * self.monthly_payments * self.sale_price() / 100)
    
    def monthly_value(self):
       return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months        

    def total_value(self):
       return self.sale_price() + self.sale_price() * self.vehicle.LEASE_RATE / self.length_in_months
    
    def monthly_value(self):
       return self.total_value() / self.length_in_months