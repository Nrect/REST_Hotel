import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import HotelRooms


# ? вернуть json без использования drf.
class RoomRecord(View):
    def get(self, request):
        # ? 1 вариант
        rooms = list(HotelRooms.objects.values())
        data = json.dumps(rooms)
        # ? 2 вариант
        # rooms = HotelRooms.objects.all()
        # data = serializers.serialize("json", rooms)
        print(data)
        # return HttpResponse(data)
        return JsonResponse(data, safe=False)
