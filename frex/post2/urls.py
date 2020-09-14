from django.urls import path
from . import views

app_name = 'post2'

urlpatterns = [
    path('', views.post, name='post2'),
    path('<id>/', views.detail, name='detail2'),
]
