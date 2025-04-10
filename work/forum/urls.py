
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.forum_view, name="forum"),
    path('<int:pk>/', views.ArticlesDatailView.as_view(), name='news-detail'),

    path('techsupport/', views.techsupport_form_view, name='techsupport_form'),
    path('techsupport/waiting', views.techsupport_waiting_view, name='techsupport_waiting'),
    path('techsupport/<int:pk>', views.techsupport_record_view, name='techsupport_record'),
    path('techsupport/closed', views.techsupport_closed_view, name='techsupport_closed'),
    path('techsupport/my-tickets', views.techsupport_user_tickets_view, name='techsupport_user_tickets'),

    path('complaints/', views.complaints_form_view, name='complaints_form'),
    path('complaints/waiting', views.complaints_waiting_view, name='complaints_waiting'),
    path('complaints/closed', views.complaints_closed_view, name='complaints_closed'),
    path('complaints/my-complaints', views.complaints_user_tickets_view, name='complaints_user_tickets'),
    path('complaints/<int:pk>', views.complaints_record_view, name='complaints_record'),
]