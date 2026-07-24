# Part 3

## Added Footer section with Contact and About page
- in base.html, added footer section and moved contact there from nav
- Added about.html, created its view and slug
- Attached it to footer as well

## Ordering Categories
- In Category model added ordering field (default = 0)
- In Meta of same added a tuple
- Run makemigrations and migrate

## Ordering Products
- In product model add date_added field with auto_now_add set to True (for adding data automatically)
- set ordering in meta to -date_added since we want descending
- Run make migrations and migrate
- terminal will ask for default for this new field, select 1 and timezone.now

## Featured Products
- Add a field in Product model as is_featured
- Then filter frontpage view products to only get is_featured

## Create Cart App
- make folder apps/cart
- startapp cart there and update settings.py

## Cart.html and View
- create templates/cart.html
- render a view for that

## TODO
-Create a footer and move "Contact" link down
-Create an about page
-Make it possible to set ordering for the categories
-Add ordering to products, newest first
-Only show featured products on the frontpage
-Create folder and app for the cart
-Create a view for the cart and show link in the menu