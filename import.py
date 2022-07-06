# from excel import make_car as mc
from excel import add
from excel import Car, Luxury_Car
from excel import ElectricCar as EC
# from excel import Luxury_Car

my_tesla = Luxury_Car('tesla', 'model s', 2019)
my_beetle = EC('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # excel.py 288
my_tesla.battery.get_range() # excel.py 297
my_new_car = Car('audi', 'a4', 2019)
# info=mc('China','Gunda',color='red')
# print(info)
print(add(1))
print(my_new_car.get_descriptive_name())
# print(my_car)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()