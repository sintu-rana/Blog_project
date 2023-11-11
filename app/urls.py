from django.urls import path, include
from .import views

# from myapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/<int:id>/', views.view_post, name='view_post'),
    

]