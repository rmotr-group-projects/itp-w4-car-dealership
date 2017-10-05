class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        if self.customer.is_employee():
            discount = 1 - self.customer.discount
        else:
            discount = 1
        return discount * (self.vehicle.sale_price() + (self.vehicle.interest_rate*self.monthly_payments*self.vehicle.sale_price()/100))
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        if self.customer.is_employee():
            discount = 1 - self.customer.discount
        else:
            discount = 1
        lease_multiplier = (self.vehicle.sale_price()*self.vehicle.lease_multiplier)/self.length_in_months
        return discount*(self.vehicle.sale_price()+lease_multiplier)
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months