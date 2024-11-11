from django.urls import path
from . import views

app_name = 'flex'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("new_item/", views.new_item, name="new-item"),
    path("edit_item/<int:pk>/", views.edit_item, name="edit-item"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path('delete/<int:pk>/', views.delete_view, name="delete"),
    path('search/', views.search, name='search'),
]