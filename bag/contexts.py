from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount_delta = 0
    more_spend = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total > settings.MINIMUM_SPEND_THRESHOLD:
        delivery = 0
        discount_delta = 50
        grand_total = delivery + total - discount_delta
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        grand_total = delivery + total
        more_spend = 350 - total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_delta': discount_delta,
        'more_spend': more_spend,
        'minimum_spend_threshold': settings.MINIMUM_SPEND_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
