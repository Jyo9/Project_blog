from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart-items/', CartItemViews.as_view())
]