from django.shortcuts import render

from. models import Category, Product


def store(request):

    all_products = Product.objects.all() # Get all products from the database

    context = {'all_products': all_products} # Create a dictionary with all products

    return render(request, 'store/store.html', context=context) # Render the store.html template with the context dictionary


def categories(request):
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}

