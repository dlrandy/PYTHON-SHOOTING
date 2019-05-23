class Battery:
  """a model for an electronic"""
  def __init__(self, battery_size = 75):
    self.battery_size = battery_size
  def describe_battery(self):
    print(f"this car has a {self.battery_size}")








