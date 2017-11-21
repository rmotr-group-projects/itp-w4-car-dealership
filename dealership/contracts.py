class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.payment = monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass
