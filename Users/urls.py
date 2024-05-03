from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.login,name = 'login'),
    path('profile/<int:user_id>',views.userprofile,name = 'userprofile'),
    path('profile/<int:user_id>/edit/',views.editprofile,name = 'editprofile'),
]