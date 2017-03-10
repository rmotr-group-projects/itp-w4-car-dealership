class Contract(object):
    pass
   
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.customer = customer
        self.vehicle = vehicle
        self.monthly_payments = monthly_payments
        
        
    def total_value(self):
        total_val = self.vehicle.sale_price() + (self.vehicle.interest * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee() is True: 
            return total_val * 0.9
        else:
            return total_val
            
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        
class LeaseContract(Contract):
    
    def __init__(self, vehicle, customer, length_in_months):
        self.customer = customer
        self.vehicle = vehicle
        self.length_in_months = length_in_months
    
    def total_value(self):
        total_val = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months) 
        if self.customer.is_employee() is True:
            return total_val * 0.9
        else:
            return total_val
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
            


"""The total_value() of a LeaseContract will be computed in this way: vehicle.sale_price() + (lease_multiplier) - (discount if employee) *.
In this case lease_multiplier depends on the vehicle and is computed in the following way:

Car: sale_price() + (sale_price() * 1.2 / length_in_months).
Motorcycle: sale_price() + (sale_price() * 1 / length_in_months)
Truck: sale_price() + (sale_price() * 1.7 / length_in_months)
The monthly_value of the contract will be just the total value divided by the amount of months: total_value() / length_in_months."""