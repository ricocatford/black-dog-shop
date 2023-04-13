from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view for rendering shopping bag """

    return render(request, 'bag/shopping-bag.html')


def add_to_bag(request, item_id):
    """ Add products to the bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    bag = request.session.get('bag', {})

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect('products')


def update_bag(request, item_id):
    """ Update products in the bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    bag = request.session.get('bag', {})

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the  bag """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)