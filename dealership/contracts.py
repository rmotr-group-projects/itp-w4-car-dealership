class Contract(object):
    def __init__(self, customer, vehicle):
        self.customer = customer
        self.vehicle = vehicle
        self.interest = {
            'Car': 1.07,
            'Motorcycle': 1.03,
            'Truck': 1.11
        }
        if self.customer.is_employee():
            self.discount = 0.10
        else:
            self.discount = 0.0

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        Contract.__init__(self, customer, vehicle)
        self.monthly_payments = monthly_payments

    def total_value(self):
        class_type = type(self.vehicle).__name__
        sale_price = self.vehicle.sale_price()

        prev_total = sale_price + \
        (self.interest[class_type] * self.monthly_payments * sale_price / 100)
        return prev_total - (prev_total * self.discount)


    def monthly_value(self):
        return round(self.total_value() / self.monthly_payments,3)

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, customer, vehicle)
        self.length_in_months = length_in_months
        self.multiplier = {
            'Car': 1.2,
            'Motorcycle': 1,
            'Truck': 1.7
        }

    def total_value(self):
        class_type = type(self.vehicle).__name__
        multiplier = self.vehicle.sale_price() * self.multiplier[class_type] / self.length_in_months
        return self.vehicle.sale_price() + multiplier - self.discount

    def monthly_value(self):
        return round(self.total_value() / self.length_in_months,3)
