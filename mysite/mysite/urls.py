from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.secret_page, name='secret_page'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
