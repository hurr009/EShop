from django.urls import path, reverse
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views, forms


urlpatterns = [
    path('', views.IndexView.as_view(template_name='authentication/index.html'), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
       
]
