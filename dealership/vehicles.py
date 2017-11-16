# things to try: make it DRYer by implementing sale_price and purchase_price
# methods into Vehicle class, rather than repeating in each type of vehicle.

class Vehicle(object):
    
    # sale multipliers 
    
    car_sale_mult = 1.2
    motorcycle_sale_mult = 1.1
    truck_sale_mult = 1.6
    
    # purchase multipliers 
    
    car_purchase_mult = 0.004
    motorcycle_purchase_mult = 0.009
    truck_purchase_mult = 0.02
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
        
class Car(Vehicle):
    
    interest_rate = 1.07
    lease_multiplier = 1.2
    
    def sale_price(self):
        return int(self.base_price * Vehicle.car_sale_mult)
        
    def purchase_price(self):
        final = self.sale_price()
        return final - (Vehicle.car_purchase_mult * self.miles)


class Motorcycle(Vehicle):
    
    interest_rate = 1.03
    lease_multiplier = 1
    
    def sale_price(self):
        return int(self.base_price * Vehicle.motorcycle_sale_mult)
        
    def purchase_price(self):
        final = self.sale_price()
        return final - (Vehicle.motorcycle_purchase_mult * self.miles)


class Truck(Vehicle):
    
    interest_rate = 1.11
    lease_multiplier = 1.7
    
    def sale_price(self):
        return int(self.base_price * Vehicle.truck_sale_mult)
        
    def purchase_price(self):
        final = self.sale_price()
        return final - (Vehicle.truck_purchase_mult * self.miles)
    
