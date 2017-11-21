class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle 
        self.customer = customer 
        self.monthly_payments = monthly_payments
    
    def discount_car(self, vehicle_price): 
        return vehicle_price - vehicle_price * .1
        
    def total_value(self):
        if self.vehicle.is_car() and self.customer.is_employee() == False:
            return self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
        elif self.vehicle.is_car() and self.customer.is_employee() == True:
           car_price = self.vehicle.sale_price() + (1.07 * self.monthly_payments * self.vehicle.sale_price() / 100)
           return self.discount_car(car_price)
        elif self.vehicle.is_motorcycle() and self.customer.is_employee() == False:
           return self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
        elif self.vehicle.is_motorcycle() and self.customer.is_employee() == True:
           bike_price = self.vehicle.sale_price() + (1.03 * self.monthly_payments * self.vehicle.sale_price() / 100)
           return self.discount_car(bike_price)
        elif self.vehicle.is_truck() and self.customer.is_employee() == False:
           return self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
        elif self.vehicle.is_truck() and self.customer.is_employee():
           truck_price = self.vehicle.sale_price() + (1.11 * self.monthly_payments * self.vehicle.sale_price() / 100)
           return self.discount_car(truck_price)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        
    
        
class LeaseContract(BuyContract, Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
    
    def total_value(self):
        if self.vehicle.is_car() and self.customer.is_employee() == False:
            car_multiplier = self.vehicle.sale_price() * 1.2 / self.length_in_months
            car_price = self.vehicle.sale_price() + car_multiplier
            return car_price 
        elif self.vehicle.is_car() and self.customer.is_employee() == True:
            self.discount_car(car_price)
        elif self.vehicle.is_motorcycle() and self.customer.is_employee() == False:
           bike_multiplier = self.vehicle.sale_price() * 1 / self.length_in_months
           bike_price = self.vehicle.sale_price() + bike_multiplier
           return bike_price
        elif self.vehicle.is_motorcycle() and self.customer.is_employee() == True:
           self.discount_car(bike_price)
        elif self.vehicle.is_truck() and self.customer.is_employee() == False:
           truck_multiplier = self.vehicle.sale_price() * 1.7 / self.length_in_months
           truck_price = self.vehicle.sale_price() + truck_multiplier
           return truck_price
        elif self.vehicle.is_truck() and self.customer.is_employee():
           self.discount_car(truck_price)
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months