from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.hotel.models import HotelRooms, BookingRoom
from api.hotel.serializer import (HotelRoomsSerializer, BookingRoomSerializer, BookingRoomListSerializer,
                                  HotelRoomsSerializer2)


class HotelRoomsList(generics.ListAPIView):
    """Список номеров отеля"""
    permission_classes = [permissions.AllowAny]
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer


class BookingRoomList(generics.ListAPIView):
    """Список забронированных номеров"""
    permission_classes = [permissions.IsAdminUser]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomListSerializer


class BookingRoomRecord(generics.CreateAPIView):
    """Запись брони в БД"""
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer


class HotelView(APIView):
    """Вывод всех номеров"""
    def get(self, request):
        rooms = HotelRooms.objects.all()
        ser = HotelRoomsSerializer(rooms)
        return Response(ser.data)


class BookingRoomRecordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request):
        # ? - data=request.data - это request.POST
        room = BookingRoomSerializer(data=request.data)
        entry_date = request.data.get("entry_date")
        depart_date = request.data.get("depart_date")
        print(entry_date)
        print(depart_date)
        if room.is_valid():
            room.save(user=request.user)
        return Response(status=201)

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]


class HotelRoomView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer


class HotelDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        rooms = HotelRooms.objects.filter(id=pk)
        ser = HotelRoomsSerializer(rooms, many=True)
        return Response(ser.data)


class HotelViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = HotelRooms.objects.all()
        serializer = HotelRoomsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = HotelRooms.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = HotelRoomsSerializer(user)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class Emp(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = HotelRooms.objects.all()
        return Response({
            "code": 200,
            "nameRu": HotelRoomsSerializer(queryset, many=True).data,
            "nameKk": HotelRoomsSerializer2(queryset, many=True).data
        })
