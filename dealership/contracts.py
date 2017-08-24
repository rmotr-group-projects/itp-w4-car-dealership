from .vehicles import Car, Truck, Motorcycle
class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments


class BuyContract(Contract):
    MULTIPLIER_DICT = {Car: 1.07,Motorcycle: 1.03,Truck: 1.11}
    
    def total_value(self): 
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + (self.MULTIPLIER_DICT[self.vehicle.__class__] * self.monthly_payments * self.vehicle.sale_price() / 100)) * .9

        else:
            return self.vehicle.sale_price() + (self.MULTIPLIER_DICT[self.vehicle.__class__] * self.monthly_payments * self.vehicle.sale_price() / 100)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    MULTIPLIER_DICT = {Car: 1.2,Motorcycle: 1,Truck: 1.7}
    
    def __init__(self, vehicle, customer,length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer, length_in_months)
        self.length_in_months = length_in_months

    def total_value(self):
        if self.customer.is_employee():
            _sale_price = self.vehicle.sale_price() 
            multiplier = self.MULTIPLIER_DICT[self.vehicle.__class__] / float(self.length_in_months)
            discount = .9
            return (_sale_price + (_sale_price * multiplier)) * discount

        else: 
            _sale_price = self.vehicle.sale_price() 
            multiplier = self.MULTIPLIER_DICT[self.vehicle.__class__] / float(self.length_in_months)
            return _sale_price + (_sale_price * multiplier)
            
    def monthly_value(self):
        return self.total_value() / self.length_in_months
