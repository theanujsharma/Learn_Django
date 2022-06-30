from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("applaud",views.applaud,name="applaud"),
    path('event', views.event, name="event"),
    path("<str:name>",views.error,name="error")
]