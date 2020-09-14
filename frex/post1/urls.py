from django.urls import path
from . import views

app_name = 'post1'

urlpatterns = [
    path('', views.post, name='post1'),
    path('<id>/', views.detail, name='detail1'),
]
