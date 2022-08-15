from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='home'),
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('coins/', views.get_coin_list, name='coin'),
    path('coins/close/<str:name>/<str:start_date>/', views.get_coin_close, name='close'),
    path('coins/profit/<str:name>/<str:start_date>/<str:end_date>/', views.get_coin_profit, name='profit')
]