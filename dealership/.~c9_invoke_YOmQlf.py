class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
    


class BuyContract(Contract):
    def monthly_value(sel):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
        def total_value():
            total = vehicle.sale_price() + (vehicle.INTEREST_RATE * monthly_payments * vehicle.sale_price() /100)
            if customer.is_employee():
                total = total * 0.9
            return total

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract).__init__(vehicle, customer)
        self.length_in_months = length_in_months 
        
    def total_value(self):
        total = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER / self.length_in_months)
        if self.customer.is_employee():
            total = total * 0.9
        return total
'''
total_value
vehicle.sale_price() + (lease_multiplier) - (discount if employee)
lease multiplyer
sale_price() + (sale_price() * LEASE_MULTIPLIER / length_in_months)
'''