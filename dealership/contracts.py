class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value(self):
        raise NotImplementedError("total_value() not implemented")


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        value = self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)
        return value if not self.customer.is_employee() else value - (value * 0.1)

    def monthly_value(self):
        return self.total_value() / self.monthly_payments if self.monthly_payments != 0 else 0


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        value = self.vehicle.sale_price() + self.vehicle.lease_multiplier(self.length_in_months)
        return value if not self.customer.is_employee() else value - (value * 0.1)

    def monthly_value(self):
        return self.total_value() / self.length_in_months if self.length_in_months != 0 else 0
