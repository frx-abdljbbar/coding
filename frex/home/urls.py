from django.urls import path
from . import views
from django.contrib.auth import views as v_iews
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', v_iews.LoginView.as_view(), name='login'),
]
