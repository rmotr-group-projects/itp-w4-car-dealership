from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    
    def __init__(self, vehicle, customer):
       self.vehicle = vehicle
       self.customer = customer
        
        # if customer.is_employee() == True:
        #     self.sale_price = (self.total_value * 0.9)
       
        # else:
        #     self.sale_price = self.total_value


class BuyContract(Contract):
    
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
    
    def total_value(self):
        
        
        if isinstance(self.vehicle, Car):
            tara = self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
            if self.customer.is_employee():
                return tara * 0.90000000
            else:
                return tara
            
        
        elif isinstance(self.vehicle, Truck):
            
            yana = self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
            if self.customer.is_employee():
                return yana * 0.9
            else:
                return yana
        
        elif isinstance(self.vehicle, Motorcycle):
            danny = self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
            
            if self.customer.is_employee():
                return danny * 0.9
            else:
                return danny

    def monthly_value(self):
        return (self.total_value() / self.monthly_payments)

#The total_value() of a BuyContract will be computed in this way: 
#vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee). 

class LeaseContract(Contract):
    
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
         
    def total_value(self):
        
        if isinstance(self.vehicle, Car):
            jason_rocks = self.vehicle.sale_price() + (self.vehicle.sale_price() * (1.2 / self.length_in_months))
            if self.customer.is_employee():
                return jason_rocks * 0.9
            else:
                return jason_rocks
    
    
        elif isinstance(self.vehicle, Truck):
            santiago = self.vehicle.sale_price() + (self.vehicle.sale_price() * (1.7 / self.length_in_months))
            if self.customer.is_employee():
                return santiago * 0.9
            else:
                return santiago
                
        elif isinstance(self.vehicle, Motorcycle):
            martin = self.vehicle.sale_price() + (self.vehicle.sale_price() * (1.0 / self.length_in_months))
            
            if self.customer.is_employee():
                return martin * 0.9
            else:
                return martin
            
            
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        
