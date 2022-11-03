from django.urls import path
from . import views
from knox import views as knox_views

app_name = 'auth'

urlpatterns = [
    path('register/',  views.RegisterView.as_view(),  name = 'register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    


]