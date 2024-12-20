from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_csv_and_analyze, name='upload_csv_and_analyze'),

]
