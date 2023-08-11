from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.LoginPageView.as_view(), name='login'),
    path('register/',views.register_user, name='register'),
    path('logout/',views.logout_user, name='logout'),

    path('search/',views.Search.as_view(), name='search'),
]
