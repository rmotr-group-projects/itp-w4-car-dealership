class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        print("This is going to fix everything!")


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass
