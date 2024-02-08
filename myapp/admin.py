# myapp/admin.py

from django.contrib import admin
from .models import Service, SubService, Appointment ,ContactMessage

admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Appointment)
admin.site.register(ContactMessage)
