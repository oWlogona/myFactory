from django.urls import path
from products import views

urlpatterns = [
    path("", views.product_brand_list, name="brand_list"),
    path("<str:brand>/", views.brand_detail, name="brand_detail"),
]
