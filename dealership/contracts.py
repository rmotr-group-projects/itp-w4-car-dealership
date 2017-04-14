from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle
class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    def total_value(self):
        if type(self.customer) is Employee:
            if type(self.vehicle) is Car:
                totalcon = (self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9 #- (.1 * self.vehicle.sale_price())
                return totalcon
            elif type(self.vehicle) is Motorcycle:
                totalcon = (self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)) *0.9 #- (.1 * self.vehicle.sale_price())
                return totalcon
            elif type(self.vehicle) is Truck:
                totalcon = (self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)) * 0.9 #(.1 * self.vehicle.sale_price())
                return totalcon
        else:
            if type(self.vehicle) is Car:
                totalcon = self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
                return totalcon
            elif type(self.vehicle) is Motorcycle:
                totalcon = self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
                return totalcon
            elif type(self.vehicle) is Truck:
                totalcon = self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
                return totalcon
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    def total_value(self):
        if type(self.customer) is Employee:
            if type(self.vehicle) is Car:
                leaseMulti = self.vehicle.sale_price() * 1.2 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti) * 0.9
            elif type(self.vehicle) is Motorcycle:
                leaseMulti = self.vehicle.sale_price() * 1 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti) * 0.9
            elif type(self.vehicle) is Truck:
                leaseMulti = self.vehicle.sale_price() * 1.7 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti) * 0.9
        else:
            if type(self.vehicle) is Car:
                leaseMulti = self.vehicle.sale_price() * 1.2 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti)
            elif type(self.vehicle) is Motorcycle:
                leaseMulti = self.vehicle.sale_price() * 1 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti)
            elif type(self.vehicle) is Truck:
                leaseMulti = self.vehicle.sale_price() * 1.7 / self.length_in_months
                return (self.vehicle.sale_price() + leaseMulti)
    def monthly_value(self):
        return self.total_value() / self.length_in_months