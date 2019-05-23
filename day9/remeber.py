import json


def get_stored_username():
  """Get stored username if available"""
  filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username

# def greet_user():
#   """Greet the user by name"""
#   try:
#     with open(filename) as f:
#       username = json.load(f)
#   except FileNotFoundError:
#     username = input('what is your name?\n')
#     with open(filename, 'w') as f:
#       json.dump(username, f)
#       print(F"we'll remeber you when you back, {username}")
#   else:
#     print(f"welcome back, {username}!")

def get_new_username():
  """Prompt for a new username"""
  username = input('what is your name? \n')
  filename = 'username.json'
  with open(filename, 'w') as f:
    json.dump(username, f)
  return username

def greet_user():
  """Greet the user by name"""
  username = get_stored_username()
  if username:
    print(f"welcome back, {username}!")
  else:
    username = get_new_username()
    print(f"we'll remeber you when you come back, {username}")

greet_user()








