class Contract(object):
    def total_volue(self):
        raise NotImplementedError
        
    def monthly_value(self):
        raise NotImplementedError
     
    interest_rate = 0
    discount = 0
    lease_multiplier = 0


class BuyContract(Contract):
    
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle=vehicle
        self._vehicle_class_name = vehicle.__class__.__name__
        self.customer=customer
        self.monthly_payments=monthly_payments
    
    def total_value(self):
        if str(self.vehicle.__class__) == 'Car':
            interest_rate = 1.07
        elif str(self.vehicle.__class__) == 'Motorcycle':
            interest_rate = 1.03
        elif str(self.vehicle.__class__) == 'Truck':
            interest_rate = 1.11

        if str(self.customer.__class__) == 'Customer':
            discount=0.1

        return (self.vehicle.sale_price() + ((self.interest_rate * self.monthly_payments * self.vehicle.sale_price()) / 100) - self.discount)
        

    def monthly_value(self):
        return (self.total_value() / self.monthly_payments)

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle=vehicle
        self.customer=customer
        self.length_in_months=length_in_months
        
    def total_value(self):

        if str(self.vehicle.__class__) == 'Car':
            lease_multiplier = 1.2
        elif str(self.vehicle.__class__) == 'Motorcycle':
            lease_multiplier = 1
        elif str(self.vehicle.__class__) == 'Truck':
            lease_multiplier = 1.7
        
        if str(self.customer.__class__) == 'Customer':
            discount = 0.1
    
        return (self.vehicle.sale_price() * (self.lease_multiplier - self.discount))
        
    def monthly_value(self):
        return (self.total_value() / self.length_in_months)