
from django.urls import path
from.import views
urlpatterns =[
    path('',views.index,name='index'),
    path('item_add/',views.item_add,name='item_add'),
    path('item_show/',views.item_show,name='item_show'),
    path('order_add/',views.order_add,name='order_add'),
    path('order_show/',views.order_show,name='order_show'),
    path('sale_show/',views.sale_show,name='sale_show'),
    path('<int:id>/item_delete/',views.item_delete,name='item_delete'),
    path('<int:id>/order_delete/',views.order_delete,name='order_delete'),
]