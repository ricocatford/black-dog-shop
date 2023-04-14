from django import template

register = template.Library()
@register.filter(name='calc_subtotal')

def calc_subtotal(price, quantity):
    """ Calculate subtotal(s) of current item(s) in the shopping bag """

    return price * quantity