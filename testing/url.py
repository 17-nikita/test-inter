from django.urls import path
from testing.views import Product
urlpatterns = [
    path("product/analytics/",Product.as_view())
]