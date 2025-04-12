from django.urls import path, re_path
from chats.consumers import ChatApp

websocket_urlpatterns = [
    re_path(r"ws/wsc/$", ChatApp.as_asgi()),
]