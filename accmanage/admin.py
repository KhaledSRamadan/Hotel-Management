from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accmanage.forms import CustomUserCreationForm,CustomUserChangeForm
from accmanage.models import CustomUser
from .models import guest
from .models import manager,staff,reception


class CustomUser_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','password1','password2','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','is_superuser','is_staff','img')
        }),
    )
    fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','is_superuser','is_staff','img')
        }),

        )
    list_display = ['username','type']

class CustomStaff_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = staff

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','password1','password2','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),
    )
    fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),

        )
    list_display = ['username','type']

class CustomManager_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = manager

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','password1','password2','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),
    )
    fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),

        )
    list_display = ['username','type']

class CustomGuest_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = guest

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','password1','password2','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),
    )
    fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),

        )
    list_display = ['username','type']

class CustomRecep_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = reception

    add_fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','password1','password2','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),
    )
    fieldsets=(
        (None, {
           'classes':('wide',),
           'fields':('first_name','last_name','username','email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')
        }),

        )
    list_display = ['username','type']


admin.site.register(CustomUser, CustomUser_Admin)
admin.site.register(guest,CustomGuest_Admin)
admin.site.register(manager,CustomManager_Admin)
admin.site.register(staff,CustomStaff_Admin)
admin.site.register(reception,CustomRecep_Admin)