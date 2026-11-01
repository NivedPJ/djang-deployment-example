from django.urls import path
from django.urls import include
from basic_app import views 

#templagte tagging

app_name = 'basic_app'
urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    
    ]
