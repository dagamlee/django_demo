from django.urls import path
from . import views

app_name="landing"
urlpatterns = [
    
     path('', views.index, name="home"),
     path('<str:month>/', views.months)

     # path('<str:name>/',views.detail)
]
