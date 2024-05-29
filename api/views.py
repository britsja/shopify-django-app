from django.http import JsonResponse
from shopify_app.decorators import session_token_required
from shopify_auth.decorators import login_required

import shopify
import logging

logger = logging.getLogger(__name__)

@login_required
def products(request, *args, **kwargs):
    logger.info(f"products triggered in api with request: {{request}}")
    with request.user.session:
        products = shopify.Product.find()

    return JsonResponse({'products': [p.to_dict() for p in products]})

@login_required
def orders(request, *args, **kwargs):
    logger.info(f"orders triggered in api with request: {{request}}")
    with request.user.session:
        orders = shopify.Order.find(status='any')

    return JsonResponse({'orders': [o.to_dict() for o in orders]})
