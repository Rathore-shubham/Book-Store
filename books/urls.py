from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('<int:book_id>/update/', views.book_update, name='book_update'),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
]