# Non-Local Scope in Python
def shopping():
  total_price = 0           # This variable has a nonlocal scopes.

  def add_item(price):
    nonlocal total_price
    total_price += price
    print(f"Item added with price: Rs.{price}. Total price: Rs.{total_price}")

  return add_item

add_to_cart = shopping()
add_to_cart(120)
add_to_cart(504)
add_to_cart(206)