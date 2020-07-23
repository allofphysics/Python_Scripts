from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Q

from django.utils.safestring import mark_safe
import json


class IndexView(generics.ListAPIView):
    template_name = "messaging/index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class RoomView(generics.ListAPIView):
    template_name = "messaging/room.html"

    def get(self, request, room_name="lobby", *args, **kwargs):
        print("ROOMVIEW", request)
        # context = {}

        return render(
            request,
            self.template_name,
            {"room_name_json": mark_safe(json.dumps(room_name))},
        )

    def post(self, request, *args, **kwargs):
        pass
