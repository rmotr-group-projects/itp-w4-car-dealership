class Contract(object):
    def total_value(self):
        discount_multiplier = 1 - self.customer.DISCOUNT
        return discount_multiplier * (self.vehicle.sale_price() + self._ttl_additive())
    
    def monthly_value(self):
        return self.total_value() / self._monthly_attribute


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        self._monthly_attribute = monthly_payments
    
    def _ttl_additive(self):
        return self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price() / 100

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        self._monthly_attribute = length_in_months

    def _ttl_additive(self):
        return (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER) / self.length_in_months