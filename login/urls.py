from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('select/', views.select_view, name='select'),
]
