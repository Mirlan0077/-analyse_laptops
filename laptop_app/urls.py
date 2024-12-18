from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.analyze_laptops, name='analyze_laptops'),
]
