class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles, multiplier):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price= base_price
        self.miles = miles
        self.multiplier = multiplier

    def sale_price(self):
        return self.base_price * self.multiplier['sale']

    def purchase_price(self):
        return self.sale_price() - (self.multiplier['purchase'] * self.miles)

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        car_multiplier = {
            'sale': 1.2 ,
            'purchase': 0.004
        }
        Vehicle.__init__(self, maker, model, year, base_price, miles, car_multiplier)

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        moto_multiplier = {
            'sale': 1.1,
            'purchase': 0.009
        }
        Vehicle.__init__(self, maker, model, year, base_price, miles,moto_multiplier)


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        truck_multiplier = {
            'sale': 1.6,
            'purchase': 0.02
        }
        Vehicle.__init__(self, maker, model, year, base_price, miles, truck_multiplier)
