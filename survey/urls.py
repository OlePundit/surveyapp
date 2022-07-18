from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns= [
    path('', views.index, name='index'),
    path('businesses', views.businesses, name='businesses'),
    path('register', views.register, name='register'), 
    path('login', views.login, name='login'), 
    path('survey/<str:pk>', views.survey, name='survey')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)