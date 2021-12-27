from django.urls import path
from .import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about_us/', views.about_us, name='about_us'), 
  path('vision_and_mission/', views.vision_and_mission, name='vision_and_mission'),  
  path('contact_us/', views.contact_us, name='contact_us'), 
  path('why_choose_us/', views.why_choose_us, name='why_choose_us'),
  path('form_submit/', views.form_submit, name='form_submit'),
  path('thank_you/', views.thank_you, name='thank_you'),
  path('our_services/<slug:cat>/', views.our_services, name='our_services'), 
    
]