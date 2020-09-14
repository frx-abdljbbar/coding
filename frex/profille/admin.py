from django.contrib import admin
from .models import Profile


admin.site.site_header = 'Codex-Frex Admin'
admin.site.site_title = 'Codex Frex'
admin.site.index_title = 'Frex Admin'


admin.site.register(Profile)
