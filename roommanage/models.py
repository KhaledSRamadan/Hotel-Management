from django.db import models
from accmanage.models import CustomUser,guest
from datetime import datetime,date,timedelta


 #Create your models here.
class service(models.Model):
	Name=models.CharField( ('Name'),max_length=50,default='new_service')
	price=models.IntegerField(default=20)
	description=models.CharField( ('description'),max_length=100,default='')
	def __str__(self):
	 	return self.Name


class hotel(models.Model):
	Name=models.CharField( ('Name'),max_length=50,default='new_hotel')
	img=models.ImageField(upload_to='static/images/')
	show=models.BooleanField(default=False)
	Location=models.CharField( ('Location'),max_length=50)
	description=models.CharField( ('description'),max_length=500,default='')
	def __str__(self):
	 	return self.Location

class room(models.Model):
	Room_ID=models.CharField( ('ID'),max_length=15,default=' ')
	class roomviews(models.TextChoices):
		Pool_View='Pool View'
		Sea_View='Sea View'

	view=models.CharField( ('View'),max_length=50,choices=roomviews.choices)
	#roomserv=models.BooleanField['WIFI','AC','TV','KITCHEN','KETTLE','MICROWAVE','MINIBAR','BATHTUB']
	breakfast=models.BooleanField(default=False)
	class BedChoices(models.TextChoices):
		One_bed='One Bed'
		Two_beds='Two Beds'
		Three_beds='Three Beds'
	room_type=models.CharField(max_length=50,choices=BedChoices.choices,default=BedChoices.One_bed)
	Room_Img=models.ImageField(upload_to='static/images/')
	status=models.BooleanField(default=False)
	price=models.IntegerField(default=20)
	Hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
	
	
	
	# def __str__(self):
	#  	return str(self.id)
	

# class service(models.Model):
# 		Name=models.CharField( ('Name'),max_length=50,default='new_service')
# 		price=models.IntegerField(default=20)
# 		description=models.CharField( ('description'),max_length=100,default='')


class reservation(models.Model):
	arrivedate=models.DateField()
	leavedate=models.DateField()
	roomid=models.ForeignKey(room,on_delete=models.CASCADE)
	guestid= models.ForeignKey(guest,on_delete=models.CASCADE)
	serviceid=models.ManyToManyField(service,blank=True)
	amount=models.IntegerField(blank=True,null=True)
	services=[]

	def __int__(self):
		return self.id







	# def __str__(self):
	#  	return self.i




	
