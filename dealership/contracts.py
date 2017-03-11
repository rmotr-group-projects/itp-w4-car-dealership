from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    #needs a __init__
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
    #total_value() is the total value of the contract to pay by a customer.
        price = self._total_value()
        if self.customer.is_employee():
            return price * .9
        return price
            

    def monthly_value(self):
    #monthly_value() is the amount of money that a customer is supposed to pay monthly.
        return self.total_value() / self._monthly_attribute()
        
class BuyContract(Contract):
    VEHICLE_MULTIPLIERS = {
        Car: 1.07,
        Motorcycle: 1.03,
        Truck: 1.11
    }

    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def _total_value(self):
        sale_price = self.vehicle.sale_price()
        multiplier = self.VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        price = sale_price + (multiplier * self.monthly_payments * sale_price / 100)
        return price
        ##vehicle.sale_price() + (I * monthly_payments * sale_price() / 100)

    def _monthly_attribute(self):
        return self.monthly_payments

class LeaseContract(Contract):
    VEHICLE_MULTIPLIERS = {
        Car: 1.2,
        Motorcycle: 1,
        Truck: 1.7
    }

    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def _total_value(self):
        sale_price = self.vehicle.sale_price() 
        multiplier = self.VEHICLE_MULTIPLIERS[self.vehicle.__class__]
        
        return (sale_price + (sale_price * multiplier / self.length_in_months))
        
    def _monthly_attribute(self):
        return self.length_in_months