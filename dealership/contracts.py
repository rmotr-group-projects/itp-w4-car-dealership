class Contract(object):
    def total_volue(object):
        raise NotImplementedError
        
    def monthly_value(object):
        raise NotImplementedError
        


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle=vehicle
        self.customer=customer
        self.monthly_payments=monthly_payments
    
    def total_volue(object):
        if self.vehicle == Car:
            interest_rate=1.07
        elif self.vehicle == Motorcycle:
            interest_rate=1.03
        elif self.vehicle== Truck:
            interest_rate=1.11
        
        if self.customer=employee:
            discount=0.1
        else:
            discount=0
        
        total_value_buy = self.sale_price + ((interest_rate - discount) * self.sale_price * self.monthly_payments )//100)
        
        return total_value_buy
        
    def monthly_value(object):
        return self.total_value / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle=vehicle
        self.customer=customer
        self.length_in_months=length_in_months
        
    def total_volue(object):
        If self.vehicle == Car:
            lease_multiplier=1.2
        elif self.vehicle == Motorcycle:
            lease_multiplier=1
        elif self.vehicle== Truck:
            lease_multiplier=1.7
        
        if self.customer=employee:
            discount=0.1
        else:
            discount=0
    
    total_value_lease = self.sale_price + (self.sale_price * lease_multiplier - discount)
    
    return total_value_lease
        
    def monthly_value(object):
        return self.total_value / self.monthly_payments
