from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('add/added',views.added,name="added"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    path('edit/<pk>/',views.edit,name='edit'),
    path('edit/<pk>/update/',views.update,name="update"),
    path('search/',views.search,name="search"),
    path('filter/',views.filter,name="filter")
    
]