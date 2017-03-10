#virtualenv = car-dealership
from dealership.vehicles import Car, Motorcycle, Truck

class Contract(object):
        
    def lease_multiplier(self):
        if isinstance(self.vehicle, Car):
            self._lease_multiplier = (self.vehicle.sale_price() * 1.2 / self.length_in_months)
        elif isinstance(self.vehicle, Motorcycle):
            self._lease_multiplier = (self.vehicle.sale_price() * 1 / self.length_in_months)
        else:
            self._lease_multiplier = (self.vehicle.sale_price() * 1.7 / self.length_in_months)
        
        return self._lease_multiplier


class BuyContract(Contract):
    #vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        self._total_value = self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            self._total_value = 0.90 * self._total_value
        return self._total_value

    def monthly_value(self):
        self._monthly_value = self.total_value()/self.monthly_payments
        return self._monthly_value
    


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    def total_value(self):
        self._total_value = self.vehicle.sale_price() + self.lease_multiplier()
        if self.customer.is_employee():
            self._total_value = 0.90 * self._total_value
        return self._total_value

    def monthly_value(self):
        self._monthly_value = self.total_value()/self.length_in_months
        return self._monthly_value
