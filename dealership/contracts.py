

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    
    def total_value(self):
        return customer.sale_price(self)
    def monthly_value(self):
        return self.total_value() / self.length_in_months()
    

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = monthly_payments
        
        
        ##vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
    def total_value(self):
        Price = self.vehicle.sale_price() + (self.vehicle.I * self.length_in_months * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            Price -= Price  * 0.1
        return Price
            
    def monthly_value (self):
        return self.total_value() / self.length_in_months
        
        

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self):
        lease_price = self.vehicle.sale_price() +  (self.vehicle.sale_price() * self.vehicle.lease_multiplier /self.length_in_months)
        if self.customer.is_employee():
            lease_price -= lease_price *0.1
        return lease_price
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
