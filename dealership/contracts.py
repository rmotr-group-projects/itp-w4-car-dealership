class Contract(object):
    pass
   
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    # total_value = Vehicle.sale_price() + (self.interest * self.__class__.monthly_payments * Vehicle.sale_price / 100) )
    # monthly_value(): total_value() / monthly_payments = $16,926 / 12 = $1,410.50
    def total_value(self):
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + (self.vehicle.interest_multiplier * self.monthly_payments * self.vehicle.sale_price() / 100)) *.9
        else:
            return self.vehicle.sale_price() + (self.vehicle.interest_multiplier * self.monthly_payments * self.vehicle.sale_price() / 100)
         
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

#vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
    
    def total_value(self):
        if self.customer.is_employee():
            return (self.vehicle.sale_price() + self.lease_multiplier()) * .9
        else:
            return self.vehicle.sale_price() + self.lease_multiplier()

    def lease_multiplier(self):
        return (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months)


#    total_value(): sale_price() + (sale_price() * 1.7 / length_in_months) = $35,000 + (35,000 * 1.7 / 36) = $36,652.77
#    monthly_value(): total_value() / monthly_payments = $36,652.78 / 36 = $1,018.13


# Car: sale_price() + (sale_price() * 1.2 / length_in_months).
# Motorcycle: sale_price() + (sale_price() * 1 / length_in_months)
# Truck: sale_price() + (sale_price() * 1.7 / length_in_months)