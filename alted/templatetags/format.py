import re
from decimal import Decimal

from django import template

register = template.Library()


@register.filter(is_safe=True)
def format_round_fiat(value):
    """
    Convert an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    if type(value) is Decimal:
        value = int(value)

    return insert_comma(value)


@register.filter(is_safe=True)
def format_fiat(value):
    return insert_comma(round(value, 2))


def insert_comma(value):
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r'\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return insert_comma(new)
