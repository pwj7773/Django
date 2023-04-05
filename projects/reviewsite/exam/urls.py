from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movie_add/',views.movie_add,name='movie_add'),
    path('<int:id>/info/',views.info,name='info'),
    path('<int:id>/review_add/',views.review_add,name='review_add'),
    path('<int:id>/load_review/',views.load_review,name='load_review'),
    path('<int:id>/movie_update/',views.movie_update,name='movie_update'),
    path('<int:id>/movie_delete/',views.movie_delete,name='movie_delete'),
]