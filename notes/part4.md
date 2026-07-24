# Part 4

## Rename cart to cart_detail
- update views.py function to new name
- update in urls.py where used

## Settings for cart
- add SESSION_COOKIE_AGE to 86400 (1 day)
- add CART_SESSION_ID to 'cart' (anything for now)

## Creating cart class
- create a files cart.py
- added add and save function in it

## Add products to cart
- create api.py in store app
- added api_add_to_cart function
- added api in urls.py
- used vue component to use addToCart function
- used add function from cart instance 


## Remove products to cart
- added api_remove_from_cart function
- added api in urls.py
- used vue component to use removeFromCart function
- used remove function from cart instance (using product id)

## Misc
- updated cart.html to display products and option to remove it
- update product_detail.html to have a add to cart button


## TODO
-Rename cart view to cart_detail
-Add two settings for the cart in the settings file
-Create a Cart class
-Make it possible to add products to the cart
-Make it possible to remove products from the cart