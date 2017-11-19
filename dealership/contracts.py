class Contract(object):
    def total_value():
        raise NotImplementedError
    
    def monthly_value():
        raise NotImplementedError


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

    def total_value(self):
        total_value = self.vehicle.sale_price() + \
            (self.vehicle.MONTHLY_INTEREST_RATE * \
            self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            total_value -= (total_value * 0.1)
        return total_value
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        total_value = self.vehicle.sale_price() + \
        (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER \
        / self.length_in_months)
        if self.customer.is_employee():
            total_value -= (total_value * 0.1)
        return total_value
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months


