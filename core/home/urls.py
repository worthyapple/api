  #created_by_me
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import proxy_view


urlpatterns = [
    path('', views.home),
    path('student',views.post_student),
    path('studentdata',views.get_student),
    path('register',views.registeruser.as_view()),
    path('proxy/', proxy_view, name='proxy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    

]