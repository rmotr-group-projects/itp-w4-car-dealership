class Contract(object):
    def __init__(self, 
                 vehicle, 
                 customer, 
                 monthly_payments = None, 
                 length_in_months = None):
        self.vehicle = vehicle
        self.customer = customer
        self.month = monthly_payments or length_in_months
        
    def monthly_value(self):
        return round(self.total_value() / self.month, 2)


class BuyContract(Contract):
    interest_multi = 1
    
    def total_value(self):
        base_sale = (self.vehicle.sale_price() 
                     + (self.vehicle.interest_multi 
                     * self.month
                     * self.vehicle.sale_price())
                     / 100)
        if self.customer.employee:
            return base_sale * 0.9
        return base_sale


class LeaseContract(Contract):
    lease_multi = 1
    
    def total_value(self):
        base_sale = (self.vehicle.sale_price()
                     + (self.vehicle.sale_price() 
                     * self.vehicle.lease_multi)
                     / self.month)
        if self.customer.employee:
            return base_sale * 0.9
        return base_sale
