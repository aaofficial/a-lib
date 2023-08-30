from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.menu_view, name='dashboard'),
    path('add/', views.add_view, name='addpost'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
