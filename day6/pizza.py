def make_pizza(size, *toppings):
  """toppings list"""
  print(f"{size} --- {toppings}")

  for top in toppings:
    print(f"- {top}")
