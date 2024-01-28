from django.urls import path
from . import views
from .views import create_customer, create_order, order_list, login_view, update_order, delete_order

urlpatterns = [
    path ('', views.index, name="index.html"),
    path ('aboutus/', views.aboutus, name="aboutus.html"),
    path ('contactus/', views.contactus, name="contactus.html"),
    path('create_customer/', create_customer, name='create_customer'),
    path('order/', create_order, name='order'),
    path('orderlist/', order_list, name='admin'),
    path('login/', login_view, name='login'),
    path('update_order/<int:pk>/', update_order, name='update_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),


    ]