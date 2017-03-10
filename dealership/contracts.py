from .vehicles import Car, Truck, Motorcycle
from .customers import Customer, Employee

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments


    def total_value(self):
        sale_price = self.vehicle.sale_price()
        
        if self.vehicle.__class__ == Car:
            price = sale_price + (1.07 * self.monthly_payments * sale_price / 100)
        elif self.vehicle.__class__ == Motorcycle:
            price = sale_price + (1.03 * self.monthly_payments * sale_price / 100)
        elif self.vehicle.__class__ == Truck:
            price = sale_price + (1.11 * self.monthly_payments * sale_price / 100)
        
        if self.customer.is_employee():
            return price - (price * 0.1)
        else:
            return price

    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months


    def total_value(self):
        sale_price = self.vehicle.sale_price()

        if self.vehicle.__class__ == Car:
            price = sale_price + (sale_price * 1.2 / self.length_in_months)
        elif self.vehicle.__class__ == Motorcycle:
            price = sale_price + (sale_price * 1 / self.length_in_months)
        elif self.vehicle.__class__ == Truck:
            price = sale_price + (sale_price * 1.7 / self.length_in_months)
        
        if self.customer.is_employee():
            return price - (price * 0.1)
        else:
            return price


    def monthly_value(self):
        return self.total_value() / self.length_in_months
