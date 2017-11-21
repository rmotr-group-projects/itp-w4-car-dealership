class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        self.discount = None
        
        if customer.is_employee():
            self.discount = .90
        else:
            self.discount = 1
            

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
            
    
    def total_value(self):
        if self.vehicle.__class__.__name__ == 'Car':
            return (self.vehicle.sale_price() + (1.07 * self.monthly_payments * \
            self.vehicle.sale_price() / 100)) * self.discount
        elif self.vehicle.__class__.__name__ == 'Truck':
            return (self.vehicle.sale_price() + (1.11 * self.monthly_payments * \
            self.vehicle.sale_price() / 100)) * self.discount
        else:
            return (self.vehicle.sale_price() + (1.03 * self.monthly_payments * \
            self.vehicle.sale_price() / 100)) * self.discount
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        

    def total_value(self):
        if self.vehicle.__class__.__name__ == 'Car':
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * \
            1.2 / self.length_in_months)) * self.discount
        if self.vehicle.__class__.__name__ == 'Truck':
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * \
            1.7 / self.length_in_months)) * self.discount
        else:
            return (self.vehicle.sale_price() + (self.vehicle.sale_price() * \
            1 / self.length_in_months)) * self.discount
    
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
    
    