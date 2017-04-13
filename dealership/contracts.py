class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

    
    def total_value(self):
        
        
        
        #check if employee, if so multiply by 0.9
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + ((self.vehicle.interest_rate * self.vehicle.sale_price() * self.monthly_payments) / 100)) * 0.9
        else:
            return self.vehicle.sale_price() + ((self.vehicle.interest_rate * self.vehicle.sale_price() * self.monthly_payments) / 100)
        

        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer 
        self.length_in_months = length_in_months
        

    
    def total_value(self):
        
        
        #check if employee, if so multiply by 0.9
        
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + self.lease_multiplier()) * 0.9
        else:
            return self.vehicle.sale_price() + self.lease_multiplier()
        
        
    def lease_multiplier(self):
        return (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months)
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months