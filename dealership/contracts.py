## import customers
## import vehicles


class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    def total_value(self):
        if self.customer.is_employee():
            return ((self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price()/100)) * .90)
        else:
            return (self.vehicle.sale_price() + (self.vehicle.I * self.monthly_payments * self.vehicle.sale_price()/100))
    
    def monthly_value(self):
        return BuyContract.total_value(self)/self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    #sale_price() + (sale_price() * 1.2 / length_in_months)
    def total_value(self):
        lease_multiplier = self.vehicle.sale_price() + ((self.vehicle.sale_price()*self.vehicle.L)/self.length_in_months)
        if self.customer.is_employee():
            return lease_multiplier*.90
        else:
            return lease_multiplier
    
    def monthly_value(self):
        return (LeaseContract.total_value(self)/ self.length_in_months)
        
## vehicle.sale_price() + (lease_multiplier) - (discount if employee) * 
# price = saleprice + (saleprice*multiplier/lengthinmonths)
# multiplier Vehicle.L