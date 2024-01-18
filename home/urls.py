from django.urls import path
from .import views

urlpatterns = [
    path('',views.home1,name='home'),
    path('about',views.about_page,name='about'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('register',views.register_page,name='register'),
    path('product/<int:pk>',views.product_page,name='product')
    
]
