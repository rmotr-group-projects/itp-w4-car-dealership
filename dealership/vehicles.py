class Vehicle(object):
    '''Class representing a vehicle.'''
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        self.sale_multiplier = None
        self.purchase_multiplier = None
        
    def sale_price(self):
        '''Gets the sale price a customer pays for a vehicle.'''
        if self.sale_multiplier:
            return self.base_price * self.sale_multiplier
        raise NotImplementedError()

    def purchase_price(self):
        '''Gets the purchase price a dealership pays for a vehicle.'''
        if self.purchase_multiplier and self.sale_multiplier:
            return self.sale_price() - (self.purchase_multiplier * self.miles)
        raise NotImplementedError()


class Car(Vehicle):
    '''Subclass of vehicle representing a car.'''
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.2
        self.purchase_multiplier = 0.004


class Motorcycle(Vehicle):
    '''Subclass of vehicle representing a motorcycle.'''
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.1
        self.purchase_multiplier = 0.009
        

class Truck(Vehicle):
    '''Subclass of vehicle representing a truck.'''
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.sale_multiplier = 1.6
        self.purchase_multiplier = 0.02
