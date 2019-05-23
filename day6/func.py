# def greet_user(user_name):
#   '''Displaty a
#    simple greeting.'''
#   print(f"hello! {user_name.upper()}")

# greet_user('boboda')


# def desc_pet(type , name="asfd"):
#   """Display info about a pet"""
#   print(f"\nI have a {type}")
#   print(f"My {type}'s name is {name}'")

# desc_pet('hamster', 'harry')
# desc_pet('dog', 'willie')

# desc_pet(type='gg', name='mm')
# desc_pet(name='xx', type='yy')

# desc_pet(type='ppap')


# def get_formatted_name(first_name,last_name,middle_name=''):
#   """return a fullname, neatly formatted."""
#   full_name = f"{first_name} {middle_name} {last_name}"
#   return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# while True:
#   print("\nPlease tell me your name:")
#   f_name = input("First name: ")
#   if f_name == 'q':
#     break
#   l_name = input("Last name: ")
#   if l_name == 'q':
#     break
#   formatted_name = get_formatted_name(f_name, l_name)
#   print(f"\nHello, {formatted_name}!")

# def greet_users(users):
#     """print a simple greeting to each users in the lise"""
#     for name in users:
#       msg = f"Hello, {name.title()}"
#       print(msg)

# user_names =  ['hannah', 'ty', 'margot']
# greet_users(user_names)
# def print_models(unprints, completes):
#   """print"""
#   while unprints:
#     cd = unprints.pop()
#     print(f"print mpdel: {cd}")
#     completes.append(cd)

# def show_completed_models(models):
#   """show models"""
#   print("\nthe following modeslk have been printed")
#   for m in models:
#     print(m)
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

from pizza import make_pizza as mp
import pizza as pp
pp.make_pizza(12, 'pepperoni')
pp.make_pizza(45, 'mushrooms', 'green peppers', 'extra cheese')

mp(45, 'mushrooms2', 'green peppers2', 'extra cheese2')


def build_profile(first, last, **user_info):
    """building"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
