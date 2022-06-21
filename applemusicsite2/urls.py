from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('signup/',views.insert,name='signup'),
    path('features/',views.features,name='features'),
    path('catalogue/',views.catalogue,name='catalogue'),
    path('login/',views.login,name='login'),
]
