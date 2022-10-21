from django.urls import path, include
from django.conf import settings
from .import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('about', views.about, name="about-us"),
    path('blog', views.blog,name="blog"),
    path('contact', views.contact,name="contact"),
    path('projects', views.projects,name="projects"),
    path('services', views.services,name="services"),
    path('about', views.about,name="about"),

]      
