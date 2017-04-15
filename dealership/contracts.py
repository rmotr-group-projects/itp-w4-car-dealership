class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        price = self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee() == True:
            price *= 0.9
        return price
                        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def total_value(self):
        leaseprice = self.vehicle.sale_price() + ((self.vehicle.sale_price() * self.vehicle.lease_multiplier) / self.length_in_months)
        if self.customer.is_employee() == True:
            leaseprice *= 0.9
        return leaseprice
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
