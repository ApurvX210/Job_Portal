from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.register,name='register'),
    path('me/',views.currentUser,name='current_User'),
    path('me/update/',views.updateUser,name='Update_User')
]