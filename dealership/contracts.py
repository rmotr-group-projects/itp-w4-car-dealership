class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments):
        self.monthly_payments = monthly_payments
        self.vehicle = vehicle
        self.customer = customer

    # Total value of the contract to paid by the customer
    def total_value(self):
        return (self.vehicle.sale_price() + (self.vehicle.INTEREST_RATE *
                                             self.monthly_payments *
                                             self.vehicle.sale_price() / 100)) * (1 - self.customer.DISCOUNT)

    # Amount of money a customer pays monthly
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class BuyContract(Contract):
    pass
    # def __init__(self, vehicle, customer, monthly_payments):
    #    pass

    # Parent class dictates total_value method
    # Parent class dictates monthly_value method


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle,
                                            customer,
                                            length_in_months)
        self.length_in_months = length_in_months

    # Child class overrides total_value method
    def total_value(self):
        return (self.vehicle.sale_price() +
                (self.calc_lease_multiplier(self.vehicle.sale_price(),
                                            self.vehicle.LEASE_FACTOR,
                                            self.length_in_months))) * \
            (1 - self.customer.discount)

    # Child class overrides monthly_value method
    def monthly_value(self):
        return self.total_value() / self.length_in_months

    @staticmethod
    def calc_lease_multiplier(_sale_price, _lease_factor, _length_in_months):
        return _sale_price * _lease_factor / _length_in_months
