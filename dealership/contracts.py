class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    INTEREST_RATES = {'Car': 1.07, 'Motorcycle': 1.03, 'Truck': 1.11}
    
    def total_value(self):
        total_val = self.vehicle.sale_price()  \
        + (BuyContract.INTEREST_RATES[self.vehicle.__class__.__name__]  \
        * self.monthly_payments * self.vehicle.sale_price() / 100) 
        
        discount = (0 if not self.customer.is_employee() else 0.1 * total_val)
        total_val -= discount 
        
        return total_val
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    
    LEASE_MULTIPLIER = {'Car': 1.2, 'Motorcycle': 1, 'Truck': 1.7}
        
    def total_value(self):
        lease_multiplier = self.vehicle.sale_price() \
        * LeaseContract.LEASE_MULTIPLIER[self.vehicle.__class__.__name__] \
        / self.length_in_months
        
        total_val3 = self.vehicle.sale_price() + lease_multiplier
        
        return total_val3
        
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months