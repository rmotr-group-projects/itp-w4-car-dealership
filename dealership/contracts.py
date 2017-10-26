import customers 
import vehicles 

class Contract(object):
    
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
        raise NotImplementedError
    
    def monthly_value(self):
        raise NotImplementedError()


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.monthly_payments = monthly_payments
        super(BuyContract, self).__init__(vehicle, customer)
    
    def total_value(self):
        #Check the type of vehicle to set interest rate
        if type(self.vehicle) is vehicles.Car:
            I = 1.07
        elif type(self.vehicle) is vehicles.Motorcycle:
            I = 1.03
        elif type(self.vehicle) is vehicles.Truck:
            I = 1.11

        #Check if Customer is a regular Customer or Employee
        if type(self.customer) is customers.Customer:
            return self.vehicle.sale_price() + (I * self.monthly_payments * 
                self.vehicle.sale_price() / 100) 
        else:
            return (self.vehicle.sale_price() + (I * self.monthly_payments * 
                self.vehicle.sale_price() / 100)) * 0.9
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.length_in_months = length_in_months
        super(LeaseContract, self).__init__(vehicle, customer)
    
    def total_value(self):
        #Check the type of vehicle to set lease multiplier
        if type(self.vehicle) is vehicles.Car:
            lease_multiplier = self.vehicle.sale_price() * 1.2 / self.length_in_months
        elif type(self.vehicle) is vehicles.Motorcycle:
            lease_multiplier = self.vehicle.sale_price() * 1 / self.length_in_months
        elif type(self.vehicle) is vehicles.Truck:
            lease_multiplier = self.vehicle.sale_price() * 1.7 / self.length_in_months

        #Check if Customer is a regular Customer or Employee
        if type(self.customer) is customers.Customer:
            return self.vehicle.sale_price() + (lease_multiplier) 
        else:
            return (self.vehicle.sale_price() + lease_multiplier) * 0.9
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
