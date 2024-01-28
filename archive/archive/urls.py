from django.contrib import admin
from django.urls import path,include
from log import views as vr
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('',include('main.urls')),
    path('admin/', admin.site.urls),
    path('register/',vr.register,name='register'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('log/',include("django.contrib.auth.urls")),
    ]
