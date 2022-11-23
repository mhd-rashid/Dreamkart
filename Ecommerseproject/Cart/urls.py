from . import views
from django.urls import path
app_name='Cart'
urlpatterns = [

    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.Cart_Detail,name='Cart_Detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete'),


    ]