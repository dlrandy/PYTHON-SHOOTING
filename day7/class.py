# () 带不带都行
class Dog:
  """A simple to attempt to model a dog."""
  def __init__(self, name, age, gg='jj'):
    """init name and age"""
    self.name = name
    self.age = age
    self.gg = gg
  def sit(self):
    """dog sitting"""
    print(f"{self.name} is now sitting")

  def roll_over(self):
    """rolling over"""
    print(f"{self.name} rolled over")


my_dog = Dog('will', 5)

print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old {my_dog.gg}")

my_dog.sit()
my_dog.roll_over()




















