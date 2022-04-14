from django.urls import path 
from . import views 


appname='theme' 

urlpatterns = [
    path('index', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('list/write', views.write, name='write'),
    path('list/post=<int:p>', views.view, name='view'),
    path('write/', views.write, name='write'),
    path('logout/', views.logout, name='logout')

            
            
            
            
            
            
]

