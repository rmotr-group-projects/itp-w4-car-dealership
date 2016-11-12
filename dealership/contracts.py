from vehicles import *
from customers import *

class Contract(object):
    pass


class BuyContract(Contract):
    #vehicle.sale_price( vehicle.purchase_price(
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle= vehicle
        self.customer= customer
        self.monthly_payments= monthly_payments
#vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
    def total_value(self):
        if isinstance(self.vehicle,Car):
            I=1.07
        elif isinstance(self.vehicle, Truck):
            I=1.11
        elif isinstance(self.vehicle, Motorcycle): 
            I=1.03
        if self.customer.is_employee():
            discount=(self.vehicle.sale_price()+(I*self.monthly_payments*self.vehicle.sale_price()/100))*.1
        else:
            discount=0
        return self.vehicle.sale_price()+(I*self.monthly_payments*self.vehicle.sale_price()/100)-discount
    
    def monthly_value(self):
        return self.total_value()/self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle= vehicle
        self.customer= customer
        self.length_in_months= length_in_months
    
    '''
    Lease Multipliers:
    
    Car: sale_price() + (sale_price() * 1.2 / length_in_months).
    Motorcycle: sale_price() + (sale_price() * 1 / length_in_months)
    Truck: sale_price() + (sale_price() * 1.7 / length_in_months)
    '''

    def total_value(self):
        '''vehicle.sale_price() + (lease_multiplier) - (discount if employee)'''
        if isinstance(self.vehicle, Car):
            lease_multiplier = self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.2 / self.length_in_months)

        elif isinstance(self.vehicle, Motorcycle):
            lease_multiplier = self.vehicle.sale_price() + (self.vehicle.sale_price() * 1 / self.length_in_months)

        elif isinstance(self.vehicle, Truck):
            lease_multiplier = self.vehicle.sale_price() + (self.vehicle.sale_price() * 1.7 / self.length_in_months)
        
        else:
            lease_multiplier = 0
        
        
        #check if the customer is an employee. If so, apply a 10% discount on the final price
        if self.customer.is_employee():
            discount = (self.vehicle.sale_price() + lease_multiplier) * 0.1
        
        else:
            discount = 0

        return lease_multiplier - discount
    
    
    def monthly_value(self):
        '''total value / length_in_months'''
        return self.total_value() / self.length_in_months