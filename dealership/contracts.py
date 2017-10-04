class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        Contract.__init__(self, vehicle, customer,monthly_payments)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        value = (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price())/100
        total_value = self.vehicle.sale_price() + value
        
        if self.customer.is_employee():
            total_value = total_value * 0.9
            return total_value
        else:
            return total_value
            
    def monthly_value(self):
        monthly_value = BuyContract.total_value(self)/self.monthly_payments
        return monthly_value
        
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, vehicle, customer,length_in_months)
        self.length_in_months = length_in_months
        
    def total_value(self):
        total_value = self.vehicle.sale_price() + (self.vehicle.lease_mutiplier_unit * self.vehicle.sale_price())/self.length_in_months
        
        if self.customer.is_employee():
            total_value = total_value * 0.9
            return total_value
        else:
            return total_value
            
    def monthly_value(self):
        monthly_value = LeaseContract.total_value(self)/self.length_in_months
        return monthly_value
        
        
