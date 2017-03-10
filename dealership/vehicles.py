class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    
    def sale_price(self):
      # Car: sale_price() + (sale_price() * 1.2 / length_in_months).
      #     Motorcycle: sale_price() + (sale_price() * 1 / length_in_months)
        #  Truck: sale_price() + (sale_price() * 1.7 / length_in_months)
        return self.base_price * self.__class__.sale_multiplier
    
    def purchase_price(self):
        return self.sale_price() - (self.__class__.purchase_multiplier * self.miles)

#Car: 7% monthly (1.07)
#Motorcycle: 3% monthly (1.03)
#Truck: 11% monthly (1.11)

class Car(Vehicle):
    sale_multiplier = 1.2
    purchase_multiplier = 0.004
    interest_multiplier = 1.07
    lease_multiplier = 1.2


class Motorcycle(Vehicle):
    sale_multiplier = 1.1
    purchase_multiplier = 0.009
    interest_multiplier = 1.03
    lease_multiplier = 1


class Truck(Vehicle):
    sale_multiplier = 1.6
    purchase_multiplier = 0.02
    interest_multiplier = 1.11
    lease_multiplier = 1.7
