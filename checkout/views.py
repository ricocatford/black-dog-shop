from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Currently there's nothing in your bag.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MyM22A1GtiqCHDpI6b4j6ifUrE0oJLawDxBRUVVEgjDm695aqaBFqPw2NrEOZgVB0MrO6GdIvM0x4BFIq9ygaiv00wUOxVJUs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)