class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        raise NotImplementedError
    
    def purchase_price(self):
        raise NotImplementedError

class Car (Vehicle):
      
      interest_rate = 1.07
      lease_multiplier = 1.2
      def sale_price(self):
          return self.base_price*1.2
      
      def purchase_price(self):
          return self.sale_price() - (0.004*self.miles)

class Truck(Vehicle):
      interest_rate = 1.11
      lease_multiplier = 1.7
      #lease_multiplier = 1.2 / length_in_months
      
      def sale_price(self):
          return self.base_price*1.6
      
      def purchase_price(self):
          return self.sale_price() - (0.02*self.miles)

class Motorcycle(Vehicle):
      interest_rate = 1.03
      lease_multiplier = 1.0
      def sale_price(self):
          return self.base_price*1.1
      
      def purchase_price(self):
          return self.sale_price() - (0.009*self.miles)

myveh = Truck("Toyota", "Camry", 2002, 29000, 3000)
print(myveh.sale_price)