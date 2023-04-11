from django.shortcuts import render


def view_bag(request):
    """ A view for rendering shopping bag """

    return render(request, 'bag/shopping-bag.html')