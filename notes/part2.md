# Part 2 - Used Commands

## Creating 'store' app and Model - Category
- Create a folder as app/store and start app here
- Add this store app in settings.py, modified apps.py as in part 1
- Add a model in models.py of store for Category (fields - title and slug)
- Run 'makemigrations' and include migration using 'migrate'
- register this model in admin.py of store app
- execute runserver

## Adding Categories
- add 2 categories from admin panel
- to show title in admin table for which add __str__ function in models
- to fix mul categories label create a class Meta with verbose_name_plural = Categories

## Model - Product
- Create another model called Product with ref of catgory (`saulgadgets/apps/store/models.py`: refer comments)
- Run 'makemigrations' and 'migrate'
- Register Product in admin.py
- add some products from admin panel

## Adding Products
- add products in context for frontpage in views.py of apps/core
- styling of products in frontpage.html

## Creating Product Detail Page
- create a view 'product_detail' in store to render product detail 
- render it in urls.py on slug

## Adding product_detail.html
- extends base.html
- in block content show title and desc conditionaly
- add this page url in view btn of products

## Add context_processors file
- collect and render menu_categories by creating a new file
- and adding it to settings.py
- now accessible in base.html

## Creating Category Detail page
- Create file category_detail.html
- updated in urls.py product detail would require a category slug now
- and just a slug for category_detail

## TODO
-Create folder and app for the store app
-Get list of products and show on the front page
-Show detail view for a product
-Show categories in the menu
-Show detail view for a category (Title and list related products)
