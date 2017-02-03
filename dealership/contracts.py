class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)) * .9
        else:
            return self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)

    def monthly_value(self):
        return BuyContract.total_value(self) / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months)) * .9
        else:
            return self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months)
        
    def monthly_value(self):
        return LeaseContract.total_value(self) / self.length_in_months