from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    imageA = models.ImageField(null=True, blank=True)
    imageB = models.ImageField(null=True, blank=True)
    imageC = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def imageAURL(self):
        if self.imageA:
            return self.imageA.url
        elif self.image:
            return self.image.url
        else:
            return ''
        
    @property
    def imageBURL(self):
        if self.imageB:
            return self.imageB.url
        elif self.image:
            return self.image.url
        else:
            return ''
        
    @property
    def imageCURL(self):
        if self.imageC:
            return self.imageC.url
        elif self.image:
            return self.image.url
        else:
            return ''	

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.address









# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Customer(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name


# class Product(models.Model):
# 	name = models.CharField(max_length=200)
# 	price = models.FloatField()
# 	digital = models.BooleanField(default=False,null=True, blank=True)
# 	image = models.ImageField(null=True, blank=True)
# 	imageA = models.ImageField(null=True, blank=True)
# 	imageB = models.ImageField(null=True, blank=True)
# 	imageC = models.ImageField(null=True, blank=True)

# 	def __str__(self):
# 		return self.name

# 	@property
# 	def imageURL(self):
# 		try:
# 			url = self.image.url
# 		except:
# 			url = ''
# 		return url
	
# 	@property
#     def imageURL(self):
#         if self.imageA:
#            return self.imageA.url
#         elif self.image:
#            return self.image.url
#         else:
#            return ''

	



	
# 	@property
# 	def imageAURL(self):
# 		try:
# 			url = self.image.url
# 		except:
# 			url = ''
# 		return url
	
# 	@property
# 	def imageBURL(self):
# 		try:
# 			url = self.image.url
# 		except:
# 			url = ''
# 		return url
	
# 	@property
# 	def imageCURL(self):
# 		try:
# 			url = self.image.url
# 		except:
# 			url = ''
# 		return url
	
	
	

	
# 	@property
#     def imageURL(self):
#     if self.imageA:
#         return self.imageA.url
#     elif self.image:
#         return self.image.url
#     else:
#         return ''


# class Order(models.Model):
# 	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
# 	date_ordered = models.DateTimeField(auto_now_add=True)
# 	complete = models.BooleanField(default=False)
# 	transaction_id = models.CharField(max_length=100, null=True)

# 	def __str__(self):
# 		return str(self.id)
		
# 	@property
# 	def shipping(self):
# 		shipping = False
# 		orderitems = self.orderitem_set.all()
# 		for i in orderitems:
# 			if i.product.digital == False:
# 				shipping = True
# 		return shipping

# 	@property
# 	def get_cart_total(self):
# 		orderitems = self.orderitem_set.all()
# 		total = sum([item.get_total for item in orderitems])
# 		return total 

# 	@property
# 	def get_cart_items(self):
# 		orderitems = self.orderitem_set.all()
# 		total = sum([item.quantity for item in orderitems])
# 		return total 

# class OrderItem(models.Model):
# 	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
# 	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# 	quantity = models.IntegerField(default=0, null=True, blank=True)
# 	date_added = models.DateTimeField(auto_now_add=True)

# 	@property
# 	def get_total(self):
# 		total = self.product.price * self.quantity
# 		return total

# class ShippingAddress(models.Model):
# 	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
# 	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# 	address = models.CharField(max_length=200, null=False)
# 	city = models.CharField(max_length=200, null=False)
# 	state = models.CharField(max_length=200, null=False)
# 	zipcode = models.CharField(max_length=200, null=False)
# 	date_added = models.DateTimeField(auto_now_add=True)
# 	completed= models.BooleanField (default=True)

# 	def __str__(self):
# 		return self.address