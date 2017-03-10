from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, 
                 vehicle, 
                 customer, 
                 monthly_payments = None, 
                 length_in_months = None):
        self.vehicle = vehicle
        self.customer = customer
        self.month = monthly_payments or length_in_months
        
    def total_value(self):
        if self.customer.employee:
            return self.base_sale() * 0.9
        return self.base_sale()
        
    def monthly_value(self):
        return round(self.total_value() / self.month, 2)


class BuyContract(Contract):
    def base_sale(self):
        sale = (self.vehicle.sale_price() 
                + (self.vehicle.interest_multi 
                * self.month
                * self.vehicle.sale_price())
                / 100)
        return sale


class LeaseContract(Contract):
    def base_sale(self):
        sale = (self.vehicle.sale_price()
                + (self.vehicle.sale_price() 
                * self.vehicle.lease_multi)
                / self.month)
        return sale
