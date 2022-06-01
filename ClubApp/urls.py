from ClubApp import views
from django.urls import path

urlpatterns = [
    path('',views.home_view,name="home"),
    
    # footer
    path('footer/',views.footer_view,name="footer"),
    path('about/',views.about_view,name="about"),
    path('contact/',views.contact_view,name="contact"),

    
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    
    
    path('booking-seat/',views.booking_view,name="booking"),
    path('show-Booking-detailes',views.show_detailes,name="detailes"),
    
    
    path('event',views.event_detailes,name="event"),
    
    
   path('tennis-booking-detailes',views.tennis_booking,name="tennis-detailes"),
    
    # path('tennis/',views.tennis_view,name="tennis"),
    # path('tennis-info/',views.tennis_info_view,name="tennis_info"),
    
    # path('online-booking/',views.online_booking_view,name="onlinebooking"),
    
    # path('booking-display/',views.display_booking_view,name="display"),
    
    
    
    # # path('dashboard/', views.dashboard, name='dashboard'),
    
    

    
    
    # path('email/', views.email_view, name='email'),
    

]