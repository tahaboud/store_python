from django.contrib import admin
from .models import Booking, Album, Contact, Artist

# Register your models here.
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Album)
admin.site.register(Artist)
