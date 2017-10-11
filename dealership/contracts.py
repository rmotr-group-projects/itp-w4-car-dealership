class Contract(object):
    
    stored_total_value = 0


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
        if self.customer.is_employee():
            self.discount = .90
        else:
            self.discount = 1
        
    
    def total_value(self): # total value of contract paid by customer
        
        total = (self.vehicle.sale_price() + (self.vehicle.interest_rate * \
        self.monthly_payments * self.vehicle.sale_price() / 100)) * self.discount
        self.stored_total_value = total
        return total
    
    def monthly_value(self): # amount customer pays monthly
        return self.stored_total_value / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
        if self.customer.is_employee():
            self.discount = .90
        else:
            self.discount = 1
        
    def total_value(self):
        total = (self.vehicle.sale_price() + (self.vehicle.sale_price() * \
        float(self.vehicle.lease_multiplier) / self.length_in_months)) * self.discount
        self.stored_total_value = total
        return total
    
    def monthly_value(self):
        return self.stored_total_value / self.length_in_months

        
    
