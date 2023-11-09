from django.urls import path
from loginApp import views

urlpatterns = [
    path('login',views.loginPage),
]
