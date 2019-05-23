alien_0 = {
  'color': 'green',
  'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'you just earned {new_points} points')

alien_0['x'] = 0
alien_0['y'] = 24
print(alien_0)

fls = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python'
}
l = fls['sarah'].title()
print(f'Sarahz favorite language is {l}')

# print(fls['sss'])
print(fls.get('sss',''))
for k, v in fls.items():
  print(k)
  print(v)
for k in fls:
  print(k)

for name  in sorted(fls.keys()):
  print(name.title())


for name  in set(fls.values()):
  print(name.title())


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for a in aliens:
  print(a)

aliens = []
for num in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)
for alien in aliens[:5]:
  print(alien)
print('...')
print(f'total :{len(aliens)}')

for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

for alien in aliens[:5]:
  print(alien)
print('...')
print(f'total :{len(aliens)}')

pizza = {
  'crust': 'thick',
  'toppings': ['asdsa', 'sdfsds', 'retert']
}

print(f"ordered {pizza['crust']}")
for t in pizza['toppings']:
  print(t)


like_languages = {
  'jen': ['python', 'ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell']
}
for name, langs in like_languages.items():
  print(f"{name.title()}'s liked langs are:'")
  for lang in langs:
    print(f"\t{lang.title()}")


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
           'location': 'princeton',
           },
       'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
}

for name, info in users.items():
  print(f'{name}')
  full = f"{info['first']} {info['last']}"
  loc = info['location']

  print(f"\tfull name: {full.title()}")
  print(f"\tlocation: {loc.title()}")



