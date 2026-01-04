from django.urls import path
from . import views

urlpatterns = [
    path("", views.ai_chat, name="chat"),
    path("about/",views.about, name="about"),
]