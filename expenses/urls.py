from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.StatsView.as_view(), name='stats'),
]
