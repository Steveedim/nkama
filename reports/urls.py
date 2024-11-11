from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
    path('create/', views.create_report, name='create_report'),
    path('view/', views.view_reports, name='view_reports'),
]
