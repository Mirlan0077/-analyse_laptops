from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),  # Маршрут для страницы "О проекте"
    path('', views.analyze_laptops, name='analyze_laptops'),
]
