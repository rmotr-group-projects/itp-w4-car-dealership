class Contract(object):
    pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle 
        self.customer = customer 
        self.monthly_payments = monthly_payments

    def total_value(self):
        sale_price = self.vehicle.sale_price()
        interest = self.vehicle.get_interest()
        discount = 0.1 if self.customer.is_employee() == True else 0 
        return (sale_price + (interest * self.monthly_payments * sale_price / 100)) * (1 - discount)

    def monthly_value(self):
        return (self.total_value()/self.monthly_payments)

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        sale_price = self.vehicle.sale_price()
        lease_multiplier = sale_price * self.vehicle.get_lease_price_base() / self.length_in_months
        discount = 0.1 if self.customer.is_employee() == True else 0 
        return (sale_price + lease_multiplier) * (1- discount)
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months