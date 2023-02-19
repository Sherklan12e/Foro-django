from django.urls import path, include
from . import views 
urlpatterns = [
    path("login_page/", views.login_page, name="login_page"),
    path("logout_page/", views.logout_user, name="logout_user"),
    path("register/", views.register_page, name="register_page"),
    path("my_profile/", views.my_profile, name="my_profile"),
    path("profile/<int:pk>/", views.profiles, name="profiles"),
    path("update_profile/", views.update_profile, name='update_profile'),
    
    
]
