class Contract(object):

    employee_discount = 0.1


class BuyContract(Contract):

    def __init__(self, vehicle, customer, monthly_payments):

        self.customer = customer
        self.vehicle = vehicle
        self.monthly_payments = monthly_payments

    def total_value(self):

        vehicle_sale_price = self.vehicle.sale_price()

        # get interest rate depending on vehicly type
        vehicle_type = type(self.vehicle).__name__
        if vehicle_type == 'Car':
            I_rate = 1.07

        elif vehicle_type == 'Motorcycle':
            I_rate = 1.03

        elif vehicle_type == 'Truck':
            I_rate = 1.11

        # value before any discounts
        value = vehicle_sale_price + (I_rate * self.monthly_payments * vehicle_sale_price) / 100

        # apply discount if an employee
        employee_status = self.customer.is_employee()
        if employee_status:
            return .90 * value

        else:
            return value

    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        pass

    def monthly_value(self):
        pass
