class Contract(object):
    def __init__(self,vehicle,customer):
        self.vehicle = vehicle
        self.customer = customer
        self.discount = customer.discount
    
    def total_value(self):
        # This will try final price with monthly_payments if it fails it will use length in months before returning the final price
        try:
            final_price = self.vehicle.sale_price() +(self.vehicle.interest * self.monthly_payments * self.vehicle.sale_price()/100)
        except:
            final_price = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_mulitiplier/self.length_in_months)
        return final_price - (final_price * self.discount)
        
    def monthly_value(self):
        # This will convert monthly_payments or length_in_months to months so we can return monthly value
        try:
            monthly = self.monthly_payments
        except:
            monthly = self.length_in_months
        return self.total_value()/ monthly

# Used super to limit repeated code in both Lease and Buy Contracts
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
