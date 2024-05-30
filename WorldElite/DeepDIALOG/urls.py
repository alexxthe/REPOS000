# 在APP中新建的URLS

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('summit-talk/', views.summit_talk, name='summit_talk'),
    path('leader-talk/', views.leader_talk, name='leader_talk'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('summit-talk/<int:id>/', views.summit_detail, name='summit_detail'),
]
