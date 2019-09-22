from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('products/<str:category>', views.filter_by_category, name='category'),
    path('search/', views.search, name='search'),
]
