from .vehicles import Car, Truck, Motorcycle


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value(self):
        pass

    def monthly_value(self):
        pass


class BuyContract(Contract):
    interest_rates = {
        Car: 1.07,
        Motorcycle: 1.03,
        Truck: 1.11,
    }

    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        return (self.vehicle.sale_price() + BuyContract.interest_rates[type(self.vehicle)]
                * self.monthly_payments * self.vehicle.sale_price() / 100) * (0.9 if self.customer.is_employee() else 1)

    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    lease_multiplier_percentage = {
        Car: 1.2,
        Motorcycle: 1,
        Truck: 1.7
    }

    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        return self.vehicle.sale_price() + self.get_lease_multiplier() * (0.9 if self.customer.is_employee() else 1)

    def get_lease_multiplier(self):
        return self.vehicle.sale_price() * LeaseContract.lease_multiplier_percentage[
            type(self.vehicle)] / self.length_in_months

    def monthly_value(self):
        return self.total_value() / self.length_in_months
