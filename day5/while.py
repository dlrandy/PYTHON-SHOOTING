# # current_number = 1
# # while current_number <= 5:
# #   print(current_number)
# #   current_number += 1

# message = ""
# prompt = "\ntell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program"
# # while message != "quit":
# #   message = input(prompt)
# #   print(message)

# # active = True
# # while active:
# #   message = input(prompt)
# #   if message == 'quit':
# #     active = False
# #   else:
# #     print(message)

# # while True:
# #   city = input(prompt)
# #   if city == 'quit':
# #     break
# #   else:
# #     print(f"I'd love to go go {city.title()}")


# # current_number = 0
# # while current_number < 10:
# #   current_number += 1
# #   if current_number % 2 == 0:
# #     continue
# #   print(current_number)

# unconfirmed_users =  ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#   current_user = unconfirmed_users.pop()

#   print(f"vertifying user:{current_user.title()}")
#   confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for user in confirmed_users:
#   print(user.title())


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#   pets.remove('cat')

# print(pets)

responses = {}
polling_active = True
while polling_active:
  name = input("\nWhat is your name?\n")
  response =  input("which mountain would you like to climb? \n")
  
  responses[name] = response

  repeat = input("would you like to let another person respond? (yes/on) \n")
  if repeat == 'no':
    polling_active = False

print("\n---- Poll Results ---")
for name, res in responses.items():
  print(f"{name} would llike to climb {res}")



















