from Prac8.taxi import Taxi
from Prac8.unreliable_car import UnreliableCar
from Prac8.silver_service_taxi import SilverServiceTaxi

taxi1 = Taxi("Prius 1", 100)
taxi1.drive(40)
print(taxi1, '\n Current fare: ${:.2f}'.format(taxi1.get_fare()))
taxi1.start_fare()
taxi1.drive(100)
print(taxi1, '\n Current fare: ${:.2f}'.format(taxi1.get_fare()))

car1 = UnreliableCar("Camry 1", 100, 50)
car1.drive(50)
print(car1)
car1.drive(70)
print(car1)

silvertaxi1 = SilverServiceTaxi("Hummer", 200, 2)
print(silvertaxi1, '\n Current fare: ${:.2f}'.format(silvertaxi1.get_fare()))
silvertaxi1.drive(10)
print(silvertaxi1, '\n Current fare: ${:.2f}'.format(silvertaxi1.get_fare()))
silvertaxi1.drive(50)
print(silvertaxi1, '\n Current fare: ${:.2f}'.format(silvertaxi1.get_fare()))
