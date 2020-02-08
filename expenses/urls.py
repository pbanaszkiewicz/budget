from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.StatsView.as_view(), name='stats'),
    path('expenses/', views.StatsView.as_view(), name='expenses-list'),
    path('categories/', views.StatsView.as_view(), name='categories-list'),
]
