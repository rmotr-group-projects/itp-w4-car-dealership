class Contract(object): ## tried to add vehicle and Person class

    def total_value(self):
        raise NotImplementedError
        
    def monthly_value(self):
        raise NotImplementedError


class BuyContract(Contract):

    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        #employee_check = self.customer.is_employee()

    def total_value(self):
        #`vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
        pre_totalvalue = self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)
        if self.customer.is_employee():
            return pre_totalvalue - ((pre_totalvalue*10)/100) #// discount over total price
        return pre_totalvalue
            
    def monthly_value(self):
        return self.total_value()/self.monthly_payments
    

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months

    def total_value(self): 
        # `vehicle.sale_price() + (lease_multiplier) - (discount if employee)
        totalvalue_lcontract_total = self.vehicle.sale_price() + (self.vehicle.sale_price()*self.vehicle.lease_multiplier/self.length_in_months)

        if self.customer.is_employee() :
           return totalvalue_lcontract_total - ((totalvalue_lcontract_total*10)/100)
        return totalvalue_lcontract_total

    def monthly_value(self):
        return (self.total_value() / self.length_in_months)