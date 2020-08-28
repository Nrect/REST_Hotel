from rest_framework import serializers

from backend.hotel.models import HotelRooms, HotelFields, RatingsRooms, BookingRoom


class HotelFieldsSerializer(serializers.ModelSerializer):
    """Поля номеров"""

    class Meta:
        model = HotelFields
        fields = ("title",
                  'sub_title',
                  "icon"
                  )


class RatingsRoomsSerializer(serializers.ModelSerializer):
    """Оценки сервиса номеров"""

    class Meta:
        model = RatingsRooms
        fields = ("title",
                  "rating"
                  )


class HotelRoomsSerializer(serializers.ModelSerializer):
    """Номера отеля"""
    # about_room = HotelFieldsSerializer(many=True)
    # about_room = serializers.StringRelatedField(many=True)
    about_room = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    services = RatingsRoomsSerializer(many=True)

    class Meta:
        model = HotelRooms
        fields = (
            "id",
            "title",
            "desc",
            "about_room",
            "services",
        )


class HotelRoomsSerializer2(serializers.ModelSerializer):
    """Номера отеля"""

    class Meta:
        model = HotelRooms
        fields = (
            "id",
            "title",
            "desc",
        )


class BookingHotelSerializer(serializers.ModelSerializer):
    """Сериализация номеров по id"""

    class Meta:
        model = HotelRooms
        fields = ("id", "title")


class BookingRoomListSerializer(serializers.ModelSerializer):
    """Сериализация списка забронированных номеров"""
    rooms = BookingHotelSerializer(read_only=True)

    class Meta:
        model = BookingRoom
        fields = (
            "entry_date",
            "depart_date",
            "name",
            "phone",
            "comment",
            "adult",
            "children",
            "rooms",
        )


class BookingRoomSerializer(serializers.ModelSerializer):
    """Бронирование номера отеля. Запись в БД"""

    class Meta:
        model = BookingRoom
        fields = (
            "entry_date",
            "depart_date",
            "name",
            "phone",
            "comment",
            "adult",
            "children",
            "rooms",
        )

    def create(self, request):
        results = request.pop('rooms')
        booking = BookingRoom.objects.create(rooms=results, **request)
        return booking
