from django.urls import path
from . import views


urlpatterns = [
    path('<str:user>/', views.profiles, name='profiles'),
    path('edit_profile/<str:user>',
         views.edit_profile, name='edit_profile'),
]