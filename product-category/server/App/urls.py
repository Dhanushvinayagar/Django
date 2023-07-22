from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('category/',views.category,name="category"),
    path('category/<int:pk>/',views.product,name="product")
]