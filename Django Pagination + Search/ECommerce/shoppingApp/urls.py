from django.urls import path
from .views import*


urlpatterns = [
    path('',index,name='index'),
    path('<int:id>/',detail,name='detail'),
]
