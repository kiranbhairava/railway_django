from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person-list'),
    path('create/', views.person_list, name='person-detail'),
]