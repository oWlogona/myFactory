from django.shortcuts import render


def product_brand_list(request):
    return render(request, "product/product_category_list.html", locals())


def brand_detail(request, brand):
    return render(request, "product/category_detail.html", locals())
