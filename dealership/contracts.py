from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    """Represents a contract with the dealership. Must be implemented as a
    BuyContract or a LeaseContract."""
    def __init__(self, vehicle, customer, num_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.discount_factor = 0.90
    
    def total_value(self):
        raise NotImplementedError()
    
    def monthly_value(self):
        raise NotImplementedError()


class BuyContract(Contract):
    """Represents a contract for purchasing a vehicle."""
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer, monthly_payments)
        self.monthly_payments = monthly_payments
        
        if isinstance(self.vehicle, Car):
            self.interest_rate = 1.07
        elif isinstance(self.vehicle, Motorcycle):
            self.interest_rate = 1.03
        elif isinstance(self.vehicle, Truck):
            self.interest_rate = 1.11
    
    def total_value(self):
        """Calculates the total value of the purchasing contact."""
        value = self.vehicle.sale_price() + (self.interest_rate *
                        self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            return value * self.discount_factor
        return value
        
    def monthly_value(self):
        """Calculates the monthly payment for purchasing a vehicle."""
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    """Represents a contract for leasing a vehicle."""
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer, length_in_months)
        self.length_in_months = length_in_months
        self.lease_multiplier = self.get_lease_multiplier(vehicle)
                                  
    def total_value(self):
        """Calculates the total value of the leasing contact."""
        value = self.vehicle.sale_price() + self.lease_multiplier
        if self.customer.is_employee():
            return value * self.discount_factor
        return value
        
    def monthly_value(self):
        """Calculates the monthly payment for leasing a vehicle."""
        return self.total_value() / self.length_in_months
        
    def get_lease_multiplier(self, vehicle_obj):
        if isinstance(vehicle_obj, Car):
            self.lease_rate = 1.20
        elif isinstance(vehicle_obj, Motorcycle):
            self.lease_rate = 1
        elif isinstance(vehicle_obj, Truck):
            self.lease_rate = 1.70
        
        return (self.vehicle.sale_price() * self.lease_rate / self.length_in_months)