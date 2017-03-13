from django.conf.urls import url
from . import views


app_name = 'users'

urlpatterns = [

    # /users/signup:url to take the input from the user
    url('signup', views.signup, name='signup'),
    #/users/showdata:url to display the list of users stored on the database
    url('showdata', views.showdata, name='showdata'),
]
