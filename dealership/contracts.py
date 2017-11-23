from .customers import Customer, Employee
from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    CAR_INTEREST = 1.07
    MOTORCYCLE_INTEREST = 1.03
    TRUCK_INTEREST = 1.11

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

    def get_interest_rate(self):
        if isinstance(self.vehicle, Car):
            return Contract.CAR_INTEREST
        elif isinstance(self.vehicle, Motorcycle):
            return Contract.MOTORCYCLE_INTEREST
        elif isinstance(self.vehicle, Truck):
            return Contract.TRUCK_INTEREST

    def total_value(self):
        self.Total_Value = self.vehicle.sale_price() + (self.get_interest_rate() * self.monthly_payments * self.vehicle.sale_price()/100) # update the interest calling
        if self.customer.is_employee()== True:
            return (self.Total_Value) - (self.Total_Value*0.1)
        else:
            return self.Total_Value

    def monthly_value(self):
            return self.total_value()/self.monthly_payments 

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle= vehicle
        self.customer= customer
        self.length_in_months = length_in_months
        self.lease_multiplier = {'Car':1.2, 'Motorcycle':1, 'Truck': 1.7}

    def total_value(self):
        self.class_name = self.vehicle.__class__.__name__
        self.Total_value1 = self.vehicle.sale_price()+(self.vehicle.sale_price() * self.lease_multiplier[self.class_name])/self.length_in_months
        if self.customer.is_employee() == True:
            return self.Total_value1 - (self.Total_value1*0.1)
        else:
            return self.Total_value1
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        

