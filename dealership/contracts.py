class Contract(object):
    pass


class BuyContract(Contract):
    interest_rate = 1
    
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        base_sale = (self.vehicle.sale_price() 
                     + (self.vehicle.interest_rate 
                     * self.monthly_payments
                     * self.vehicle.sale_price())
                     /100
                     )
        if self.customer.employee:
            return base_sale*0.9
        return base_sale
        
    def monthly_value(self):
        return self.total_value()/self.monthly_payments


class LeaseContract(Contract):
    lease_multiplier = 1
    
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        base_sale = (self.vehicle.sale_price() 
                     + (self.vehicle.sale_price()
                     * self.vehicle.lease_multiplier
                     / self.length_in_months))
        if self.customer.employee:
            return base_sale*0.9
        return base_sale
    
    def monthly_value(self):
        return round(self.total_value() / self.length_in_months, 2)
    
    
    
