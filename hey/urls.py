
from django.urls import path,include
from . import views
urlpatterns = [
  
    path('',views.login,name='login'),
    path('search',views.search,name='search'),
    path('register',views.regis,name='regis'),
    path('login',views.login,name='login'),
    #path('accounts/reg',views.accr,name='accr'),
   # path('accounts/login',views.login,name='login'),
    path('check',views.check,name='check'),
    path('index',views.index,name='index'),
    path('googlelogin',views.gl,name='gl'),
    path('profile',views.profile,name='profile'),
    path('contact',views.contact,name='contact'),
    path('games',views.games,name='games')
]   
