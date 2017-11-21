class Contract(object):

    employee_discount = 0.1

    def __init__(self, vehicle, customer):
        self.customer = customer
        self.vehicle = vehicle


class BuyContract(Contract):

    # The __init__ here is required because we are extending
    # the init of the parent (Contract) class
    # Contract.__init__(self, vehicle, customer) activates the
    # attributes of the parent class

    def __init__(self, vehicle, customer, monthly_payments):
        Contract.__init__(self, vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):

        interest_rates = {'Car': 1.07, 'Motorcycle': 1.03, 'Truck': 1.11}

        vehicle_sale_price = self.vehicle.sale_price()

        # get interest rate depending on vehicly type
        I_rate = interest_rates[type(self.vehicle).__name__]

        # value before any discounts
        buycontract_value = vehicle_sale_price + (I_rate * self.monthly_payments * vehicle_sale_price) / 100

        # apply discount if an employee
        if self.customer.is_employee():
            return (1 - self.employee_discount) * buycontract_value

        else:
            return buycontract_value

    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):

    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):

        lease_multipliers = {'Car': 1.2, 'Motorcycle': 1, 'Truck': 1.7}

        vehicle_sale_price = self.vehicle.sale_price()

        lease_multiplier = lease_multipliers[type(self.vehicle).__name__]

        leasecontract_value = vehicle_sale_price + (vehicle_sale_price * lease_multiplier / self.length_in_months)

        if self.customer.is_employee():
            return (1 - self.employee_discount) * leasecontract_value

        else:
            return leasecontract_value

    def monthly_value(self):
        return self.total_value() / self.length_in_months
