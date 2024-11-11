from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_home, name='notifications_home'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('send/', views.send_notification, name='send_notifications'),
    path('view/', views.view_notifications, name='view_notifications'),
]
