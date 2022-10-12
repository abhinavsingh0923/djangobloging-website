from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('yourblog/',views.yourblog, name='yourblog'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlesignout,name='handlesignout'),
    path('logout',views.handlesignout,name='handlesignout'),
    path('search',views.search,name='search'),
    path('delete<int:sno>/',views.deleteblog,name='deleteblog'),
    path('update<int:sno>/',views.update,name='update'),
]
