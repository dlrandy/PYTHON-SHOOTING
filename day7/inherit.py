from car import Car
from battery import Battery
class ElectricCar(Car):
  """Represent aspects of a car, specific to electronic verhicles"""
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 75
    self.battery = Battery()
  def describe_battery(self):
    print(f"this car has a {self.battery_size}-kwh battery")
  def test_jj(self):
    print(f' {self} test electronic car jj')
    super().test_jj()
    print(super() == self)
  def __eq__(self, other):
    print(self)
    print(other)
    return True
car_test = ElectricCar('tesla', 'model S', 2019)
print(car_test.get_descriptive_name())
car_test.describe_battery()
car_test.test_jj()
car_test.battery.describe_battery()











