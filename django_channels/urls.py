from messaging.views import IndexView
from messaging.views import RoomView
from django.conf.urls import url
from django.urls import path, re_path

urlpatterns = [
    url(r"^$", IndexView.as_view()),
    re_path(r"^(?P<room_name>[0-9a-zA-Z]{1,20})/$", RoomView.as_view()),
]
