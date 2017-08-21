from .vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer 
        

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        # super(SubClass, self).__init__(parent class parameters)
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        # Check if customer is an employee or not,
        # then determine price based on vehicle type
        if self.customer.is_employee():
            if isinstance(self.vehicle, Car):
                return (self.vehicle.sale_price() + ((1.07 * self.monthly_payments * self.vehicle.sale_price() )/ 100)) * 0.9
            elif isinstance(self.vehicle, Motorcycle):
                return (self.vehicle.sale_price() + ((1.03 * self.monthly_payments * self.vehicle.sale_price() )/ 100)) * 0.9
            else:
                return (self.vehicle.sale_price() + ((1.11 * self.monthly_payments * self.vehicle.sale_price() )/ 100)) * 0.9
        else:
            if isinstance(self.vehicle, Car):
                return (self.vehicle.sale_price() + ((1.07 * self.monthly_payments * self.vehicle.sale_price() )/ 100))
            elif isinstance(self.vehicle, Motorcycle):
                return (self.vehicle.sale_price() + ((1.03 * self.monthly_payments * self.vehicle.sale_price() )/ 100))
            else:
                return (self.vehicle.sale_price() + ((1.11 * self.monthly_payments * self.vehicle.sale_price() )/ 100))
    
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    
    def total_value(self):
        # Check if customer is an employee or not,
        # then determine price based on vehicle type
        if self.customer.is_employee():
            if isinstance(self.vehicle, Car):
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1.2 / self.length_in_months) * 0.9
            elif isinstance(self.vehicle, Motorcycle):
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1 / self.length_in_months) * 0.9
            else:
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1.7 / self.length_in_months) * 0.9
        else:
            if isinstance(self.vehicle, Car):
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1.2 / self.length_in_months)
            elif isinstance(self.vehicle, Motorcycle):
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1 / self.length_in_months)
            else:
                return (self.vehicle.sale_price() + (self.vehicle.sale_price()) * 1.7 / self.length_in_months)
                
    def monthly_value(self):
        return self.total_value() / self.length_in_months
