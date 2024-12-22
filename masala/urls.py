from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name= "home-view"),
    path('resolve', views.resolve_kalesh, name='resolve-kalesh'),
    path('kaleshi/<str:kaleshi_slug>/', views.kaleshi_response_view, name="kaleshi-response-view")
]
