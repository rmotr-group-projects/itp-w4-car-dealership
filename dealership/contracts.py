from vehicles import *

class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.payment = monthly_payments
        print(self.vehicle)
    def total_value(self):
    	if isinstance(self.vehicle, car):
    		i = 1.07
    	if isinstance(self.vehicle, motorcycle):
    		i = 1.03
    	if isinstance(self.vehicle, truck):
    		i = 1.11
    	if isinstance(self.customer, employee):
    		d = 0.9
    	if isinstance(self.customer, customer):
    		d = 1

    	return self.vehicle.sale_price() + (i * self.payment * self.vehicle.sale_price() / 100) * d

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass

