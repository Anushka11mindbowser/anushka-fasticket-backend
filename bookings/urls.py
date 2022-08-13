from django.views import View
from django.urls import path
from bookings import views

urlpatterns = [
    path("createBooking", views.CreateBookingView.as_view(), name = "Book a Show"),
    path("getBookings", views.BookingsListView.as_view(), name="List of Bookings")
]