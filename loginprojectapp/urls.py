from django.contrib import admin
from .views import *
from django.urls import path


from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns



urlpatterns = [
    path('index', index, name='index'),
    path('user-register', register, name='register'),
    path('user-profile', user_profile, name='user_profile'),
    path('', user_login, name='user_login'),
    path('user-logout', user_logout, name='user_logout'),

    
 
]
# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


