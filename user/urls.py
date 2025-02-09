from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('home/',views.home),
    path('about/',views.about),
    path('event/', views.myevent),
    path('contact/',views.contact),
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout),
    path('viewdetails/',views.viewdetails),
    path('viewcharity/',views.viewcharity),
    path('feedback/',views.feedback),
    path('myprofile/',views.profile),
    path('soevent/',views.soevent),
    path('informal/',views.informal),
    path('charity/',views.charity),
    path('education/',views.education),
    path('vigallery/',views.vigallery),
    path('imgallery/',views.imgallery),
    path('booking/',views.booking),
    path('mybooking/',views.mybooking),
    
    

]