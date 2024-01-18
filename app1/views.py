from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import ProductDetails
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app1.forms import ProductDetailsForm,BookingForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')


def store(request):
    return render(request, 'store.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('login')


def adminproductlist(request):
    products = ProductDetails.objects.all()
    return render(request, 'adminproductlist.html', {'products': products})


def store(request):
    products = ProductDetails.objects.all()
    return render(request, 'store.html', {'products': products})


def userproductdetails(request,product_id):
    product = ProductDetails.objects.get(id=product_id)
    quantity_range = range(1, product.Stock + 1)
    return render(request, 'userproductdetails.html', {'product': product, 'quantity_range': quantity_range})


def bookproduct(request, product_id):
    product = get_object_or_404(ProductDetails, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))

        if quantity <= product.Stock:
            product.Stock -= quantity
            product.save()

            success_message = f'Successfully purchased {quantity} {product.Name}(s).'

            return render(request, 'bookproduct_success.html', {'success_message': success_message})
        else:
            error_message = 'Insufficient stock for the requested quantity.'
            return render(request, 'bookproduct_error.html', {'error_message': error_message})

    return redirect('userproductdetails', product_id=product.id)

def submitproduct(request):
    if request.method == 'POST':
        form = ProductDetailsForm(request.POST, request.FILES)
        print(form.is_valid()) 

        if form.is_valid():
            form.save()
            return redirect('adminproductlist')  
    else:
        form = ProductDetailsForm()

    return HttpResponse("Product Added")

def adminproductcreate(request):  
    return render(request, 'adminproductcreate.html')

