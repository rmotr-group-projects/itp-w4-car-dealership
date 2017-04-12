class Vehicle(object):
    """Base class for Car, Motorcycle, and Truck"""
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    SALE_MULTIPLIERS = {'Car': 1.2, 'Motorcycle': 1.1, 'Truck': 1.6}
    
    PURCHASE_MULTIPLIERS = {'Car': 0.004, 'Motorcycle': 0.009, 'Truck': 0.02}
        
    def sale_price(self):
        return self.base_price * Vehicle.SALE_MULTIPLIERS[self.__class__.__name__]
    
    def purchase_price(self):
        return self.sale_price() - (Vehicle.PURCHASE_MULTIPLIERS[self.__class__.__name__] * self.miles)



class Car(Vehicle):
    """Subclass of Vehicle (0)"""
    pass


class Motorcycle(Vehicle):
    """Subclass of Vehicle (1)"""
    pass


class Truck(Vehicle):
    """Subclass of Vehicle (2)"""
    pass
