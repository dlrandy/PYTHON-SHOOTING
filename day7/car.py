class Car:
  """A simple attempt to represent a car."""
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  def get_descriptive_name(self):
    long_name = f"{self.year} {self.model}"
    return long_name.title()
  def read_odometer(self):
    print(f"this car has {self.odometer_reading} miles on it")
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print('you can not roll back an odometer ')
  def increment_odometer(self, miles):
    self.odometer_reading += miles
  def test_jj(self):
    print(f'{self} car test jj')











