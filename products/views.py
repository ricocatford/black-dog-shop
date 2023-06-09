from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view for showing all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None
    category_name = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'


            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_name_list = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_name_list)
            category_name = category_name_list[0]
            category = Category.objects.filter(name__in=category_name_list)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_category_name': category_name,
        'current_category': category,
        'current_sorting': current_sorting
    }

    return render(request, template, context)



def product_details(request, product_id):
    """ A view for displaying products details """

    product = get_object_or_404(Product, pk=product_id)
    template = 'products/product-details.html'
    context = {
        'product': product
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ A view for adding products to the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'There was an error while adding product, please try again.')
    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view for editing products in the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'There was an error while updating product, please try again.')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view for deleting products in the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect(reverse('products'))
