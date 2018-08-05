from django.conf.urls import url
from userauth import views

app_name = 'userauth'

urlpatterns  = [
    url(r'^register/$',views.register, name='register'),
    url(r'^userlogin/$',views.user_login, name='user_login'),
]
