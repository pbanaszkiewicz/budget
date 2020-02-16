from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.StatsView.as_view(), name='stats'),
    path('expenses/', views.ExpenseList.as_view(), name='expenses'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
]
