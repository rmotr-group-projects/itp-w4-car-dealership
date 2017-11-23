from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    '''Represents a contract with the dealership. Must be implemented as a
    BuyContract or a LeaseContract.'''
    def __init__(self, vehicle, customer, num_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.discount_rate = 0.10
        
        if isinstance(self, BuyContract):
            self.monthly_payments = num_payments
        elif isinstance(self, LeaseContract):
            self.length_in_months = num_payments
        else:
            raise NotImplementedError()
    
    def total_value(self):
        raise NotImplementedError()
    
    def monthly_value(self):
        raise NotImplementedError()


class BuyContract(Contract):
    '''Represents a contract for purchasing a vehicle.'''
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer, monthly_payments)
        
        if isinstance(self.vehicle, Car):
            self.interest_rate = 0.07
        elif isinstance(self.vehicle, Motorcycle):
            self.interest_rate = 0.03
        elif isinstance(self.vehicle, Truck):
            self.interest_rate = 0.11
    
    def total_value(self):
        '''Calculates the total value of the purchasing contact.'''
        value = self.vehicle.sale_price() + ((1 + self.interest_rate) *
                        self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            return value * (1 - self.discount_rate)
        return value
        
    def monthly_value(self):
        '''Calculates the monthly payment for purchasing a vehicle.'''
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    '''Represents a contract for leasing a vehicle.'''
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer, length_in_months)

        if isinstance(self.vehicle, Car):
            self.lease_rate = 0.20
        elif isinstance(self.vehicle, Motorcycle):
            self.lease_rate = 0
        elif isinstance(self.vehicle, Truck):
            self.lease_rate = 0.70
            
        self.lease_multiplier = (self.vehicle.sale_price() * 
                                  (1 + self.lease_rate) / self.length_in_months)
                                  
    def total_value(self):
        '''Calculates the total value of the leasing contact.'''
        value = self.vehicle.sale_price() + self.lease_multiplier
        if self.customer.is_employee():
            return value * (1 - self.discount_rate)
        return value
        
    def monthly_value(self):
        '''Calculates the monthly payment for leasing a vehicle.'''
        return self.total_value() / self.length_in_months