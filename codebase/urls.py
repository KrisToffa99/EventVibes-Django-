from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.Register, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forget-password/', views.ForgetPassword, name='forget-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('event-details/', views.EventDetails, name='event-details'),
    path('event-details-temp/<int:event_id>/', views.EventDetailsTemp, name='event-details-temp'),
    path('event-ticket/', views.EventTicket, name='event-ticket'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)