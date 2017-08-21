class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    sale_multiplyer = 1.2
    purchase_multiplyer = 0.004
    
    def sale_price(self):
      return self.base_price * Car.sale_multiplyer
    
    def purchase_price(self):
      return self.sale_price() - (Car.purchase_multiplyer * self.miles)


class Motorcycle(Vehicle):
    sale_multiplyer = 1.1
    purchase_multiplyer = 0.009
    
    def sale_price(self):
      return self.base_price * Motorcycle.sale_multiplyer
    
    def purchase_price(self):
      return self.sale_price() - (Motorcycle.purchase_multiplyer * self.miles)


class Truck(Vehicle):
    sale_multiplyer = 1.6
    purchase_multiplyer = 0.02
    
    def sale_price(self):
      return self.base_price * Truck.sale_multiplyer
    
    def purchase_price(self):
      return self.sale_price() - (Truck.purchase_multiplyer * self.miles)
