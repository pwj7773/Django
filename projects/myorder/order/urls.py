from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('read/',views.read),
    path('read/<int:id>/',views.read_order),
    path('read/<int:id>/update/',views.update),
    path('read/<int:id>/delete/',views.delete),
    path('regist/',views.regist),
    path('read/search/',views.search),

]