from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from zoneinfo import ZoneInfo
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

DEFAULT_THUMBNAIL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgLNLbFmOl-wuybKGc6IrdKYGPxe62xr-wYA&s"

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "popular":
        product_list = Product.objects.all().order_by('-likes')
    elif filter_type == "highest_price":
        product_list = Product.objects.all().order_by('-price')
    elif filter_type == "lowest_price":
        product_list = Product.objects.all().order_by('price')
    else:
        product_list = Product.objects.filter(user=request.user) 

    context = {
        'npm' : '2406437262',
        'name': request.user.username,
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    try:
        products = Product.objects.all()
        data = [
            {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "price": float(p.price),
                "thumbnail": p.thumbnail if p.thumbnail else "",
                "user_id": p.user.id if p.user else None,  # <--- aman
                "likes": p.likes,
            }
            for p in products
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        print("Error fetching products:", e)
        return JsonResponse({"error": str(e)}, status=500)



def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),  # pastikan JSON friendly
            'category': product.category,
            'category_display': product.get_category_display(),
            'thumbnail': product.thumbnail.url if product.thumbnail else None,
            'is_featured': product.is_featured,
            'likes': product.likes,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def show_xml_by_id(request, id):
    try:
        product_list = Product.objects.get(pk=id)
        xml_data = serializers.serialize("xml", [product_list])
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)
    


def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "show_product.html", context)

def like_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_likes()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login_user')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            # response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('last_login', str(datetime.datetime.now(ZoneInfo("Asia/Jakarta"))))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    prod = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=prod)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    prod = get_object_or_404(Product, pk=id)
    prod.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required
@csrf_exempt
def add_product_entry_ajax(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        thumbnail = request.POST.get("thumbnail") or DEFAULT_THUMBNAIL
        category = request.POST.get("category", "men")
        is_featured = request.POST.get("is_featured") == "true" or request.POST.get("is_featured") == "on"
        user = request.user

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            user=user
        )
        return JsonResponse({
            "id": str(product.id),
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "thumbnail": product.thumbnail,
            "category": product.category,
            "is_featured": product.is_featured,
            "likes": product.likes,
            "user_id": product.user.id
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

