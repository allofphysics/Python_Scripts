from django.conf.urls import url
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"^testing/(?P<room_name>[0-9a-zA-Z]{1,20})/$", consumers.ChatConsumer)
]
