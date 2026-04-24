from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('discussion/', views.discussions_view, name='discussion'),
    path('accounts/', include('accounts.urls')),
    path('', views.cover_view, name='home'),
]