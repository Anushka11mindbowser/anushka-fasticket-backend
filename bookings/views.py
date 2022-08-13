from rest_framework.response import Response
from rest_framework import status
from .models import Bookings
from .serializers import BookingsSerializer
from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView
                                    )

# Create your views here.
class CreateBookingView(CreateAPIView):
    serializer_class = BookingsSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"New Show Booked",
                "data":serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingsListView(ListAPIView):
    serializer_class = BookingsSerializer
    permission_classes = []

    def get_queryset(self):
        bookings = Bookings.objects.all()
        return bookings

    def get(self, request, *args, **kwargs):
        bookings = self.get_queryset()
        serializer = self.serializer_class(bookings, many=True)
        response = {
            "message":"List of Bookings",
            "data":serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)