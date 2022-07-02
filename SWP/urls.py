"""SWP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from roommanage.views import rooms_view,home_view,room_view,reserapp_view, about_view, payment_value, bookings_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accmanage.views import signup, loginprocess, logoutprocess, profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('branch/<str:hotname>', rooms_view),
    path('hotelhome/',home_view),
    #path('branch/sampl',rooms_view),
    path('signup/', signup,name='signup'),
    path('login/',loginprocess,name='login'),
    path('logout/',logoutprocess,name='logout'),
    path('profile/',profile),
    path('',home_view),
    path('room/<int:roomname>', room_view),
    path('room/reserv/<int:roomname>',reserapp_view),
    path('about/', about_view,name='about'),
    path('booking/<int:bookingid>',payment_value),
    path('bookings/',bookings_view,name='mybookings'),

    # path('coco/',register_view)



]

urlpatterns+= staticfiles_urlpatterns()