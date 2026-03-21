from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('leave/', views.leave_view, name='leave'),
    path('notice/', views.notice_view, name='notice'),
    path('study-materials/', views.study_materials_view, name='study_materials'),
    path('study-materials/<str:code>/', views.subject_materials_view, name='subject_materials'),
    path('assignments/', views.assignments_view, name='assignments'),
    path('digilocker/', views.digilocker_view, name='digilocker'),
    ]

