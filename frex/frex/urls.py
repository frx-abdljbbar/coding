"""frex URL Configuration """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #..........START..........
    path('accounts/', include('django.contrib.auth.urls')),
    #.........END..............

    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('profile/', include('profille.urls', namespace='profille')),
    path('html/', include('post.urls', namespace='post')),
    path('django/', include('post1.urls', namespace='post1')),
    path('css/', include('post2.urls', namespace='post2')),
    path('python/', include('post3.urls', namespace='post3')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
