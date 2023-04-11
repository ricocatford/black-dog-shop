from django.shortcuts import render, redirect


def view_bag(request):
    """ A view for rendering shopping bag """

    return render(request, 'bag/shopping-bag.html')


def add_to_bag(request, item_id):
    """ Add products to the bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect('products')