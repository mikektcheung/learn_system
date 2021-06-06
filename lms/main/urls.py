from . import views
from django.urls import path

urlpatterns = [
    path('logout/',views.logout, name = 'logout'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),

    path('main/', views.main, name='main'),
    path('redeem/change/<int:pk>/',views.redeem_change, name = 'redeem-change'),
]