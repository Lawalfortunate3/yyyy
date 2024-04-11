from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
	path('user/', views.userPage, name="user-page"),
    path('staff/', views.staff, name="staff"),
    path('contact/', views.contact, name="contact"),
    
	path('product_details/', views.product_details, name="product_details"),

	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

    path('confirm_payment/<str:pk>', views.confirm_payment, name="confirm_payment"),
]