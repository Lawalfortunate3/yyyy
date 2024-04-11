from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
 def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        return view_func (request, *args, **kwargs)

 return wrapper_func   

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
         
            group = None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name

            if group in allowed_roles:
               return view_func(request, *args, **kwargs)
            else:
               return HttpResponse('You Are Not Autorized To View This Page...')    
        return wrapper_func  
    return decorator
      

# def admin_only(view_func):
#    def wrapper_function(request, *args, **kwargs):
#       group = None
#       if request.user.group.exists():
#       # if user.groups.filter(name='customer').exists():
#          groups = request.user.groups.all()[0].name

#       if group == 'customer':
#          return redirect('store')
      
#       if group == 'customer':
#          return view_func(request, *args, **kwargs) 
      
#    return wrapper_function
      




















# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             groups = request.user.groups.all()
#             for group in groups:
#                 if group.name in allowed_roles:
#                     return view_func(request, *args, **kwargs)
#             return HttpResponse('You Are Not Authorized To View This Page...')
#         return wrapper_func
#     return decorator

# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         groups = request.user.groups.all()
#         for group in groups:
#             if group.name == 'admin':
#                 return view_func(request, *args, **kwargs)
#         return redirect('store')
#     return wrapper_function


