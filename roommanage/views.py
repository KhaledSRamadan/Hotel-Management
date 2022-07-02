from django.shortcuts import render, redirect
from .models import room,hotel,reservation,service
from .forms import ReservationForm
from accmanage.models import CustomUser

# # Create your views here
global hotelid
def home_view(request):
	# if request.method =='POST':
	# 	hotelid=name
	hotels=hotel.objects.all()
	return render(request,"blog/index.html",{'hotels':hotels})


def rooms_view(request,hotname):
	obj=room.objects.filter(Hotel__exact=hotname)
	hotels=hotel.objects.all()
	return render(request,"blog/branch.html",{'roomiyes':obj,'hotels':hotels})

def room_view(request,roomname):
	obj=room.objects.get(id__exact=roomname)
	hotels=hotel.objects.all()
	return render(request,"blog/room.html",{'room':obj,'hotels':hotels})


def payment_value(request,bookingid):
	booking=reservation.objects.get(id__exact=bookingid)
	roomvar = room.objects.get(id__exact=booking.roomid.id)
	servicevar=0
	for each in booking.serviceid.all():
		servicevar= servicevar+each.price
	
	stay= booking.leavedate-booking.arrivedate
	stay_days=int(stay.days)
	roomprice=roomvar.price
	amount=(roomprice*stay_days)+servicevar
	
	return render(request,"blog/bookingid.html",{'services':booking.serviceid.all(),'amount':amount,'booking':booking})

def bookings_view(request):
	userid=request.user.id
	bookings=reservation.objects.filter(guestid=userid)
	amounts=[]
	for booking in bookings:
		roomvar = room.objects.get(id__exact=booking.roomid.id)
		servicevar=0
		services=[]
		for each in booking.serviceid.all():
			servicevar= servicevar+each.price
			services.append(each)

		stay= booking.leavedate-booking.arrivedate
		stay_days=int(stay.days)
		roomprice=roomvar.price
		amount=(roomprice*stay_days)+servicevar
		booking.services=services
		amounts.append(amount)
		booking.amount=amount
	
	return render(request,"blog/Allbookings.html",{'bookings':bookings,'amounts':amounts})



def reserapp_view(request,roomname):
    if request.method == 'POST':
    	if request.user.is_authenticated==0:
    		raise Http404("You must login")
    	form = ReservationForm(request.POST)
    	userid=request.user.id
    	user=CustomUser.objects.get(id__exact=userid)
    	obj=room.objects.get(id__exact=roomname)
    	if form.is_valid():
    		res=form.save(commit=False)
    		res.roomid= obj
    		res.guestid=user
    		stay= res.leavedate-res.arrivedate
    		stay_days=int(stay.days)
    		roomprice=obj.price
    		# servicevar=0
    		# for each in form.serviceid.all():
    		# 	servicevar= servicevar+each.price
    		# amount=(roomprice*stay_days)+servicevar
    		# res.amount=amount
    		form.save()
    		if res is not None:
    			return redirect('/booking/'+str(res.id))
    else:
    	form = ReservationForm()
    return render(request, 'blog/Booking.html', {'form': form, 'room':str(roomname)})

def about_view(request):
	return render(request,'blog/about.html')
