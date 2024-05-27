from django.http import JsonResponse
from shopify_app.decorators import session_token_required

import shopify
import logging

logger = logging.getLogger(__name__)

@session_token_required
def products(request):
    logger.info(f"products triggered in api")
    products = shopify.Product.find()

    return JsonResponse({'products': [p.to_dict() for p in products]})

@session_token_required
def orders(request):
    logger.info(f"orders triggered in api")
    orders = shopify.Order.find(status='any')

    return JsonResponse({'orders': [o.to_dict() for o in orders]})
