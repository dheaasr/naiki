from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_list = Product.objects.all()
    context = {
        'npm' : '2406437262',
        'name': 'Dhea Anggrayningsih Syah Rony',
        'class': 'PBP C',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_list = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_list])
        return HttpResponse(json_data, content_type="application/json")
    except:
        return HttpResponse(status=404)
    


def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, "show_product.html", context)

def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.increment_likes()
    return redirect('main')
