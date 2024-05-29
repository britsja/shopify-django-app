from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.apps import apps
from django.views.decorators.clickjacking import xframe_options_exempt
from shopify_app.decorators import known_shop_required, latest_access_scopes_required
from shopify_auth.mixins import LoginRequiredMixin
import shopify
import logging

logger = logging.getLogger(__name__)


class HomeView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):        
        context = {
            "shop_origin": kwargs.get("shopify_domain"),
            "api_key": apps.get_app_config("shopify_app").SHOPIFY_API_KEY,
            "scope_changes_required": kwargs.get("scope_changes_required"),            
        }
        logger.info(f"Context from HomeView: {{context}}")
        return render(request, "home/index.html", context)
