class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    
class BuyContract(Contract):
    
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        interest = (self.vehicle.I*self.monthly_payments*self.vehicle.sale_price()/100)
        sale_price = self.vehicle.sale_price()
        total =  sale_price + interest
        
        if self.customer.is_employee():
            return total*0.9
        else:
            return total
    def monthly_value(self):
        return self.total_value()/self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
        sale_price = self.vehicle.sale_price() 
        multiplier = self.vehicle.M
        
        total = sale_price +(sale_price*multiplier/self.length_in_months)
        if self.customer.is_employee():
            return total*0.9
        else:
            return total
   
    def monthly_value(self):
        return self.total_value()/self.length_in_months
        
        
