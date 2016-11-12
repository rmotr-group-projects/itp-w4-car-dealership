from vehicles import Car, Truck, Motorcycle
from customers import*


class Contract(object):
    pass
    # @classmethod
    # def total_value(cls):
    #     cls.vehicle.sale_price() 
    #     #BUY CONTRACT: vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
        #LEASE CONTRACT: vehicle.sale_price() + (lease_multiplier) - (discount if employee)

    #@classmethod
    # def monthly_value(cls):
    #     return cls.total_value() / cls.monthly_payments


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle=vehicle
        self.customer=customer
        self.monthly_payments=monthly_payments
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        
    
    def total_value(self):
        multiplier = 0       
        discount_percentage = 1
        
        if self.customer.is_employee():
            discount_percentage = .9       
       
        if isinstance(self.vehicle, Car):
            multiplier = 1.07
        elif isinstance(self.vehicle, Motorcycle):
            multiplier = 1.03
        else: 
            multiplier = 1.11
            
        price = self.vehicle.sale_price() + (multiplier * self.monthly_payments * self.vehicle.sale_price() / 100) 
        
        return price * discount_percentage
     
     
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle=vehicle
        self.customer=customer
        self.length_in_months=length_in_months
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months   
        
    def total_value(self):
        multiplier = 0
        discount_percentage = 1
        
        if self.customer.is_employee():
            discount_percentage = .9
            
        if isinstance(self.vehicle, Car):
            multiplier = 1.2
        elif isinstance(self.vehicle, Motorcycle):
            multiplier = 1
        else: 
            multiplier = 1.7
        
        
        price = self.vehicle.sale_price() + (self.vehicle.sale_price() * multiplier / self.length_in_months)
        
        return price * discount_percentage
            
   