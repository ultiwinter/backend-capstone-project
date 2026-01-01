from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Icecream", price=9.99, inventory=99)
        self.assertEqual(str(item), "Icecream : 9.99")
    
    def test_default_inventory(self):
        item = Menu.objects.create(title="Cake", price=4.99)
        self.assertEqual(item.inventory, 5)


class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            BookingDate=datetime(2025, 12, 31, 18, 0)
        )
        expected_str = "John Doe - 4 guests at 2025-12-31 18:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            name="Jane Doe",
            BookingDate=datetime(2025, 12, 31, 19, 0)
        )
        self.assertEqual(booking.no_of_guests, 6)