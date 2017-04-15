class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    def total_value(self):
        if self.vehicle.__class__.__name__ == 'Car':
            total = self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
        elif self.vehicle.__class__.__name__ == 'Truck':
            total = self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
        elif self.vehicle.__class__.__name__ == 'Motorcycle':
            total = self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            return total * .9
        else:
            return total
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    def total_value(self):
        if self.vehicle.__class__.__name__ == 'Car':
            total = self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.2 / self.length_in_months)
        elif self.vehicle.__class__.__name__ == 'Truck':
            total = self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.7 / self.length_in_months)
        elif self.vehicle.__class__.__name__ == 'Motorcycle':
            total = self.vehicle.sale_price() + (self.vehicle.sale_price() / self.length_in_months)
        if self.customer.is_employee():
            return total * .9
        else:
            return total
    def monthly_value(self):
        return self.total_value() / self.length_in_months
