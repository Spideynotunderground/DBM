from django.contrib import admin
from .models import qr, Receiver, Contract


# Register your models here.

admin.site.register(qr)
admin.site.register(Receiver)
admin.site.register(Contract)