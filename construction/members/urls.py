from django.urls import path
from . import views

urlpatterns = [
    path('login_page', views.login_page, name="login"),
    path('loggout_user', views.loggout_user, name='logout'),
  
]
