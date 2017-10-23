import pytest
from argparse import Namespace

from dealership.contracts import BuyContract, LeaseContract
from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

def almost_equal(x, y, places):
    return round(x-y, places) == 0

@pytest.fixture
def fixtures():
    f = Namespace()
    f.car = Car(maker='Ford', model='Mustang', year=2005,
                   base_price=18000, miles=31000)

    f.truck = Truck(maker='Chevrolet', model='Silverado', year=2014,
                       base_price=29000, miles=3000)

    f.bike = Motorcycle(maker='Ducati', model='Monster',
                           year=2016, base_price=18000, miles=700)

    f.customer = Customer('John', 'Doe', 'john@example.com')
    f.employee = Employee('Jane', 'Doe', 'jane@example.com')

    return f


def test_buy_contract_total_value_with_customer(fixtures):
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.customer, monthly_payments=6)

    assert almost_equal(car_contract.total_value(), 22986.72, places=3)
    assert almost_equal(car_contract.monthly_value(), 3831.12, places=3)

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.customer, monthly_payments=12)

    assert almost_equal(
        truck_contract.total_value(), 52580.47, places=1)
    assert almost_equal(
        truck_contract.monthly_value(), 4381.70, places=1)

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.customer, monthly_payments=36)

    assert almost_equal(bike_contract.total_value(), 27141.84, places=2)
    assert almost_equal(bike_contract.monthly_value(), 753.94, places=2)

def test_buy_contract_total_value_with_employee(fixtures):
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.employee, monthly_payments=6)

    assert almost_equal(car_contract.total_value(), 20688.04, places=1)
    assert almost_equal(car_contract.monthly_value(), 3448, places=1)

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.employee, monthly_payments=12)

    assert almost_equal(
        truck_contract.total_value(), 47322.43, places=2)
    assert almost_equal(
        truck_contract.monthly_value(), 3943.53, places=1)

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.employee, monthly_payments=36)

    assert almost_equal(
        bike_contract.total_value(), 24427.65, places=1)
    assert almost_equal(
        bike_contract.monthly_value(), 678.54, places=1)


def test_buy_contract_total_value_with_customer(fixtures):
    car_contract = LeaseContract(
        vehicle=fixtures.car, customer=fixtures.customer, length_in_months=12)

    assert almost_equal(car_contract.total_value(), 23760.0, places=3)
    assert almost_equal(car_contract.monthly_value(), 1980.0, places=3)

    truck_contract = LeaseContract(
        vehicle=fixtures.truck, customer=fixtures.customer, length_in_months=24)

    assert almost_equal(
        truck_contract.total_value(), 49686.66, places=1)
    assert almost_equal(
        truck_contract.monthly_value(), 2070.27, places=1)

    bike_contract = LeaseContract(
        vehicle=fixtures.bike, customer=fixtures.customer, length_in_months=36)

    assert almost_equal(
        bike_contract.total_value(), 20350, places=2)
    assert almost_equal(
        bike_contract.monthly_value(), 565.27, places=1)
