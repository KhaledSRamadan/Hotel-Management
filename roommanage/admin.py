from django.contrib import admin
from .models import room,hotel,reservation, service
from .forms import ReservationForm
# Register your models here.

class CustomReserv_Admin(admin.ModelAdmin):
    add_form = ReservationForm
    # form = CustomUserChangeForm
    model = reservation

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('arrivedate','leavedate','roomid','guestid','serviceid')
        }),
    )
    list_display = ['arrivedate','leavedate','roomid']


admin.site.register(hotel)
admin.site.register(room)
admin.site.register(reservation,CustomReserv_Admin)
admin.site.register(service)