from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post, name='post'),
    path('<id>/', views.detail, name='detail'),
]
