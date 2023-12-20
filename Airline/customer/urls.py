from django.urls import path
from . import views


urlpatterns = [
        # path("",views.Profile.as_view(), name="Profile"),
         path("register/",views.register.as_view(), name="register"),
         path("login/", views.Login.as_view(), name="login"),

    
]

