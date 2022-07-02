from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager 
from django.core.validators import MinValueValidator
from datetime import datetime,date
# Create your models here.
class nations(models.TextChoices):
	Egyptian="Egyptian"
	American="American"
	Portuguese="Portuguese"

class CustomUser(AbstractUser):
	class types(models.TextChoices):
		guest = "guest", "Guest"
		admina = "admina", "Admina"
		manager="manager", "Manager"
		staff="staff"
		receptionist="receptionist"
	type = models.CharField( ('Type'), max_length=50, choices=types.choices, default=types.guest )
	img=models.ImageField(upload_to='static/images/',default='202-2026524_person-icon-default-user-icon-png.png')
	userage=models.IntegerField(default=0)
	userphone=models.CharField(max_length=14,default='',blank=True)
	usercreditcard=models.CharField(max_length=16,default='',blank=True)
	creditcard_cvv=models.CharField(max_length=3,default='',blank=True)
	creditcard_ED=models.CharField(max_length=5,default='ex: 03/24',blank=True)
	
	

class guestmanager(BaseUserManager):

	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=CustomUser.types.guest)

class adminmanager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=CustomUser.types.admina)	

class managermanager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=CustomUser.types.manager)		

class staffmanager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=CustomUser.types.staff)		

class recepmanager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=CustomUser.types.receptionist)		

class manager(CustomUser):
	
	objects = managermanager()
	class Meta:
		proxy=True

class staff(CustomUser):
	
	objects = staffmanager()
	class Meta:
		proxy=True

class reception(CustomUser):
	objects = recepmanager()
	class Meta:
		proxy=True


class guest(CustomUser):
	#CreditCard=models.CharField( ('CreditCard'),max_length=16,default=' ')
	objects = guestmanager()
	class Meta:
		proxy=True
