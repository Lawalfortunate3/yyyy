from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import OrderForm, CreateUserForm
from .models import Order
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group


from django.contrib import messages
from .forms import CreateUserForm
from .decorators import unauthenticated_user
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .models import Order, Product
from .utils import cartData, guestOrder
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrderItem, ShippingAddress




@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user= form.save()
			form.save()

			username = form.cleaned_data.get('username')


			messages.success(request, username + ' Account created Successfully...')
			return redirect ('login')

	context = {'form':form}
	return render(request, 'store/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST': 
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		
		else: messages.info(request, 'Username OR Password is incorect')


	context = {}
	return render(request, 'store/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')

def userPage(request):
	context = {}
	return render(request, 'store/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def confirm_payment(request, pk):
	checkout = checkout.object.get(id=pk)
	ShippingAddress.completed = True
	checkout.save()
	messages.success(request, 'PAYMENT MADE SUCCESSFULLY')
	return redirect('store') 

def product_details(request):
	context = {}
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/product_details.html', context)

def contact(request):
	context = {}
	return render(request, 'store/contact.html', context)

def staff(request):
	context = {}
	return render(request, 'store/staff.html', context)





