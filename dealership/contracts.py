
class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

#customer is employee, discount of 10%
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract,self).__init__(vehicle,customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        sale_price = self.vehicle.sale_price()
        value = sale_price + (self.vehicle.InterestRate * self.monthly_payments * sale_price/100)
        if self.customer.is_employee():
            return value - (0.1 * value)
        return value

    def monthly_value(self):
        return self.total_value()/self.monthly_payments



class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        lease_multiplier = self.vehicle.lease_multiplier(self.length_in_months)
        value = self.vehicle.sale_price() + lease_multiplier
        if self.customer.is_employee():
            return value - (0.1 * value)
        return value


    def monthly_value(self):
        return self.total_value()/self.length_in_months

