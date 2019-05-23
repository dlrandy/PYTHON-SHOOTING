magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(f'{magician.title()} that was a great')
  print(f"i can't wait yo see your next trixk, {magician}")

  print('thank you everyone grat magic show')

message = 'hello python world'
print(message)

for value in range(1,5):
  print(value)

for val in range(6):
  print(val)


rangs = range(7)
print(rangs)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

sqaures = []
for v in range(1,11):
  square = v ** 2
  sqaures.append(square)
print(sqaures)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

sqs = [val ** 2 for val in range(0,11)]
print(sqs)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])

print(players[:4])
print(players[2:])
print(players[-3:])

print('here are the first three players on my team')
for player in players[:3]:
  print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('my favorite foods are:')
print(my_foods)
print('\nmy froends favoreite foods are:')
print(friend_foods)

my_foods.append('canopli')
friend_foods.append('ice cream')

print('my favorite foods are:')
print(my_foods)
print('\nmy froends favoreite foods are:')
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]= 250

for d in dimensions:
  print(d)

dimensions = (340,450)

for d in dimensions:
  print(d)




























