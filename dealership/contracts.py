class Contract(object):

    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
        base_contract_value = self.vehicle.sale_price() + self.get_contract_modifier()
        return base_contract_value - (0.1*base_contract_value*self.customer.is_employee())
        
    def monthly_value(self):
        return self.total_value()/self.get_monthly_modifier()
        
    def get_contract_modifier(self):
        raise NotImplementedError()
        
    def get_monthly_modifier(self):
        raise NotImplementedError()

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.monthly_payments = monthly_payments
        self.vehicle = vehicle
        self.customer = customer

    def get_contract_modifier(self):
        return (self.vehicle.get_buy_multiplier() * self.monthly_payments * self.vehicle.sale_price() / 100)

    def get_monthly_modifier(self):
        return self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.length_in_months = length_in_months
        self.vehicle = vehicle
        self.customer = customer
        
    def get_contract_modifier(self):
        return ((self.vehicle.get_lease_multiplier() * self.vehicle.sale_price())/self.length_in_months)
        
    def get_monthly_modifier(self):
        return self.length_in_months