cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print('hold the anchovies')

print('mushrooms' in requested_topping)

print('sdf' not in requested_topping)

age = 11
if age >= 18:
  print('you are old enough to vore')
  print('have you registered to vote yet')
else:
  print('you are too young')
  print('register to vote as soon as you turn 18')

if age < 4:
  print('free')
elif age < 18:
  print('25')
else:
  print('40')

rts = ['ss','dd', 'ff']
if 'ss' in rts:
  print('adding ss')
elif 'xx' in rts:
  print('xx')
elif 'ee' in rts:
  print('ee')

toppings = []
if toppings:
  for topping in toppings:
    print(f'adding {topping}')
  print('finished making pizza')
else:
  print('are you want a pizza')
















