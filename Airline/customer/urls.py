from django.urls import path
from . import views


urlpatterns = [
        path("",views.Profile.as_view(), name="profile"),
        path("register/",views.register.as_view(), name="register"),
        path("login/", views.Login.as_view(), name="login"),
        path('order/',views.OrderList.as_view(),name="order_list"),
        path('order/<int:pk>/',views.OrderDetail.as_view(),name="order_detail"),
        path('order/<int:pk>/payment/',views.Payment.as_view(),name="payment"),
        path('order/<int:pk>/cancel/',views.Cancel.as_view(),name="cancel"),
        path('edit/<int:pk>/',views.profile_update,name="edit_profile"),
        path('commentlist/',views.CommentList.as_view(),name="comment_list"),
        path('comment/<int:pk>/',views.CommentDetail.as_view(),name="comment_detail"),
        path('comment/',views.CommentView.as_view(),name="comment"),
        path('editpassword/', views.change_password, name='change_password'),
        path('confirmation/', views.confirmationView, name='confirmation'),
        path('login_with_phone/', views.LoginWithPhone.as_view(), name='login_with_phone'),
        path('login_with_phone/compare/', views.compare, name='compare'),


    
]

