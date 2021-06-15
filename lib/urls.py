from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='user'),
    path('validate', views.validate, name='validate'),
    path('logout', views.logout_request, name='logout'),
    path('ongoing', views.ongoing, name='ongoing'),
    path('index', views.index, name='index'),
    path('files', views.files, name='files'),
    path('history', views.history, name='history'),
    path('user', views.user, name='user'),
    path('signup', views.signup, name='signup')
]