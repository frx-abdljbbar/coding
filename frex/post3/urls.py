from django.urls import path
from . import views

app_name = 'post3'

urlpatterns = [
    path('', views.post, name='post3'),
    path('<id>/', views.detail, name='detail3'),
]
