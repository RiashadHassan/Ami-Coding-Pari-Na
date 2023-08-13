from django.urls import path
from . import views
urlpatterns = [
    path('', views.InputItemAPI.as_view(), name='get-data'),
    
]