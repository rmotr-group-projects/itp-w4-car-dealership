from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def interest_rate(self):
        interest_dict = {Car : 1.07, Motorcycle: 1.03, Truck : 1.11}
        return (interest_dict[type(self.vehicle)] * self.monthly_payments * self.vehicle.sale_price() / 100)
    
    def total_value(self):
        price = self.vehicle.sale_price() + self.interest_rate() 
        if not self.customer.is_employee():
            return price
        else:
            discount = price * 0.1
            return price - discount
        
    def monthly_value(self):
        return self.total_value()/self.monthly_payments
            

class LeaseContract(Contract):
    
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def lease_multiplier(self):
        lease_dict = {Car : 1.2, Motorcycle: 1, Truck : 1.7}
        return self.vehicle.sale_price() * lease_dict[type(self.vehicle)] / self.length_in_months
    
    def total_value(self):
        price = self.vehicle.sale_price() + self.lease_multiplier() 
        if not self.customer.is_employee():
            return price
        else:
            discount = price * 0.1
            return price - discount

    
    def monthly_value(self):
        return self.total_value()/self.length_in_months
