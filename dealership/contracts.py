class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = super(Contract, self).__init__()
        self.customer = super(Contract, self).__init__()
        # TODO: refactor
        self.sales_price = vehicle.sale_price()
        self.lease_multiplier = vehicle.lease_multiplier()
        self.interest_rate = vehicle.interest_rate()
        self.is_employee = customer.is_employee()
        self.discount = customer.discount

    def total_value(self):
        """This should be implemented within each class, if not raise an error"""

        raise NotImplementedError

    def monthly_value(self):
        """This should be implemented within each class, if not raise an error"""

        raise NotImplementedError


class BuyContract(Contract):
    """BuyContract inherits from Contract"""

    def __init__(self, vehicle, customer, monthly_payments):
        """Gather all necessary information for a contract"""

        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        """Calculate the total contract value to buy a vehicle"""

        total = self.sales_price + (self.interest_rate * self.monthly_payments / 100) 

        # Employees work hard and deserve a discount
        if self.is_employee:
            total = total - (total * self.discount)
        return total

    def monthly_value(self):
        """Calculate the monthly contract payments to buy a vehicle"""

        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    """LeaseContract inherits from Contract"""

    def __init__(self, vehicle, customer, length_in_months=1):
        """Gather all necessary information for a customer"""

        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        """Calculate the total contract value to lease a vehicle"""

        total = self.sales_price + (self.lease_multiplier / self.length_in_months)

        # Employees work hard and deserve a discount
        if self.is_employee:
            total = total + (total * self.discount)

        return total

    def monthly_value(self):
        """Calculate the monthly contract payments to lease a vehicle"""

        return self.total_value() / self.length_in_months
