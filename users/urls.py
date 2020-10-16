from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.get_user, name='userDetail'),
    path('list/', views.get_users_list, name='usersList')
]

