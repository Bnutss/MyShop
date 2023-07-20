from django.shortcuts import render, redirect
from seller.models import Product
from django.utils import timezone


def product_list(request):
    products = Product.objects.filter(purchase_status=False)
    return render(request, 'buyer/product_list.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'buyer/product_detail.html', {'product': product})


def buy_product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.purchase_status = True
        product.purchase_date = timezone.now()
        product.save()
        return redirect('product_list')
    else:
        return render(request, 'buyer/buy_product.html')


