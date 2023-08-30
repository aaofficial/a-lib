from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.score_view, name='anjoman'),
]
