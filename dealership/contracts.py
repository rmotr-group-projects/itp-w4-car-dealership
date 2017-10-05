class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        interest = self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100
        return (1 - (self.customer.discount if self.customer.is_employee() else 0)) * (self.vehicle.sale_price() + interest)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        lease_cost = (self.vehicle.sale_price() * self.vehicle.lease_multiplier) / self.length_in_months
        return (1 - (self.customer.discount if self.customer.is_employee() else 0)) * (self.vehicle.sale_price() + lease_cost)
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months