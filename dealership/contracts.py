from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def final_price(self):
        sale_price = self.vehicle.sale_price()
        if self.customer.is_employee():
            return sale_price * 0.9
        return sale_price

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        return self.final_price() + (self.vehicle.interest_rate() * self.monthly_payments * self.final_price() / 100)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def lease_multiplier(self):
        return self.final_price() * self.vehicle.lease_multiplier / self.length_in_months
        
    def total_value(self):
        return self.final_price() + self.lease_multiplier()
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months