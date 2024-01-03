from django.urls import path
from . import views


urlpatterns = [
         path("",views.Profile.as_view(), name="profile"),
         path("register/",views.register.as_view(), name="register"),
         path("login/", views.Login.as_view(), name="login"),
         path("logout/", views.Logout.as_view(), name="logout"),
         path('order/',views.OrderList.as_view(),name="order_list"),
         path('order/<int:pk>/',views.OrderDetail.as_view(),name="order_detail"),
         path('order/<int:pk>/payment/',views.Payment.as_view(),name="payment"),
         path('order/<int:pk>/cancel/',views.Cancel.as_view(),name="cancel"),


    
]

